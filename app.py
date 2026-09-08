# -*- coding: utf-8 -*-
"""
AI for Biology / Protein / Peptide / LLM daily research digest agent.

Usage:
    python app.py                  # run and push to WeChat
    python app.py --dry-run        # only print, do not push or update state
    python app.py --no-llm         # skip DeepSeek, use keyword rules only
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import feedparser
import requests
import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")
DEFAULT_CONFIG = ROOT / "config.yaml"
DEFAULT_STATE = ROOT / "state.json"
USER_AGENT = "Mozilla/5.0 (compatible; DailyAIBioDigest/1.0)"


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


def clean_html(value: str) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def stable_id(item: dict) -> str:
    raw = str(item.get("url") or item.get("title") or "").strip()
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def load_state(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            log(f"read state failed, rebuild: {exc}")
    return {}


def save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    tmp.replace(path)


def parse_date(entry: Any) -> Optional[datetime]:
    """Extract UTC datetime from a feedparser entry."""
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        parsed = getattr(entry, key, None)
        if parsed:
            try:
                return datetime(*parsed[:6], tzinfo=timezone.utc)
            except Exception:
                continue
    raw = entry.get("published") or entry.get("updated") or entry.get("created")
    if raw:
        try:
            parsed = feedparser.parse(raw)
            dt = parsed.get("published_parsed") or parsed.get("updated_parsed")
            if dt:
                return datetime(*dt[:6], tzinfo=timezone.utc)
        except Exception:
            pass
    return None


def load_config(path: Path) -> dict:
    if not path.exists():
        log(f"config not found: {path}")
        sys.exit(1)
    cfg = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    cfg.setdefault("keywords", [])
    cfg.setdefault("sources", [])
    cfg.setdefault("lookback_days", 3)
    cfg.setdefault("max_items_before_llm", 40)
    cfg.setdefault("max_items_final", 12)
    cfg.setdefault("use_rule_filter", True)
    cfg.setdefault("digest_name", "AI x Bio Daily Digest")
    cfg.setdefault("llm", {})
    return cfg


def get_now() -> datetime:
    return datetime.now(timezone.utc)


def _http_get(url: str, params: Optional[dict] = None, timeout: int = 30) -> bytes:
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, params=params, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.content


def fetch_arxiv(source: dict, cfg: dict, now: datetime) -> list:
    url = source.get("url") or "http://export.arxiv.org/api/query"
    params = {
        "search_query": source.get("query", ""),
        "start": 0,
        "max_results": int(source.get("max_results", 100)),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    content = _http_get(url, params=params)
    feed = feedparser.parse(content)
    items = []
    for entry in feed.entries:
        title = clean_html(entry.get("title", ""))
        summary = clean_html(entry.get("summary", ""))
        link = (entry.get("link") or entry.get("id") or "").replace("http://", "https://")
        date = parse_date(entry)
        items.append({
            "source": source.get("name", "arXiv"),
            "title": title,
            "url": link,
            "summary": summary,
            "date": date,
        })
    log(f"arXiv fetched {len(items)} items")
    return items


def fetch_rss(source: dict, cfg: dict, now: datetime) -> list:
    url = source["url"]
    content = _http_get(url, timeout=30)
    feed = feedparser.parse(content)
    items = []
    for entry in feed.entries:
        title = clean_html(entry.get("title", ""))
        summary = clean_html(entry.get("summary") or entry.get("description") or "")
        link = entry.get("link") or ""
        date = parse_date(entry)
        items.append({
            "source": source.get("name", url),
            "title": title,
            "url": link,
            "summary": summary,
            "date": date,
        })
    log(f"{source.get('name', url)} fetched {len(items)} items")
    return items


def fetch_all(cfg: dict) -> list:
    now = get_now()
    items = []
    for source in cfg["sources"]:
        try:
            stype = source.get("type", "rss")
            if stype == "arxiv":
                items.extend(fetch_arxiv(source, cfg, now))
            else:
                items.extend(fetch_rss(source, cfg, now))
        except Exception as exc:
            log(f"fetch failed for {source.get('name')}: {exc}")
    return items


def within_lookback(item: dict, cfg: dict, now: datetime) -> bool:
    days = float(cfg.get("lookback_days", 3))
    date = item.get("date")
    if date is None:
        return True
    return now - date <= timedelta(days=days)


def rule_relevant(item: dict, cfg: dict) -> bool:
    text = f"{item['title']} {item['summary']}".lower()
    for kw in cfg.get("keywords", []):
        kw = str(kw).strip().lower()
        if kw and kw in text:
            return True
    return False


def filter_and_dedupe(all_items: list, cfg: dict, state: dict, now: datetime):
    new_items = []
    seen_ids = []
    for item in all_items:
        if not within_lookback(item, cfg, now):
            continue
        if cfg.get("use_rule_filter", True) and not rule_relevant(item, cfg):
            continue
        sid = stable_id(item)
        if sid in state:
            continue
        new_items.append(item)
        seen_ids.append(sid)
    return new_items, seen_ids


def dedupe_in_memory(items: list) -> list:
    seen = set()
    out = []
    for item in items:
        key = (item.get("url") or item.get("title") or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def sort_items(items: list) -> list:
    def keyfunc(item: dict):
        date = item.get("date")
        if date is None:
            return datetime.min.replace(tzinfo=timezone.utc)
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
        return date
    return sorted(items, key=keyfunc, reverse=True)


def build_candidate_block(items: list) -> str:
    lines = []
    for idx, item in enumerate(items, 1):
        date_str = ""
        if item.get("date"):
            try:
                date_str = item["date"].strftime("%Y-%m-%d")
            except Exception:
                date_str = ""
        summary = item.get("summary", "")[:600]
        lines.append(f"<item {idx}>")
        lines.append(f"Source: {item.get('source')}")
        if date_str:
            lines.append(f"Date: {date_str}")
        lines.append(f"Title: {item.get('title')}")
        lines.append(f"Summary: {summary}")
        lines.append(f"URL: {item.get('url')}")
        lines.append("</item>")
    return "\n".join(lines)


def call_deepseek(cfg: dict, items: list) -> Optional[str]:
    llm_cfg = cfg.get("llm", {}) or {}
    if not llm_cfg.get("enabled", True):
        log("llm.enabled=false, skip DeepSeek and use rule digest")
        return None

    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        log("DEEPSEEK_API_KEY is empty, skip LLM and use rule digest")
        return None

    base_url = os.getenv("DEEPSEEK_BASE_URL", "").strip() or "https://api.deepseek.com"
    model = os.getenv("DEEPSEEK_MODEL", "").strip() or llm_cfg.get("model", "deepseek-chat")
    max_final = int(cfg.get("max_items_final", 12))

    system_prompt = llm_cfg.get("system_prompt", "You are a research assistant.")
    user_template = llm_cfg.get(
        "user_prompt",
        "Filter the candidates below. Keep at most {max_items_final} relevant items. Output Markdown.\n\n{items}",
    )
    user_prompt = user_template.format(max_items_final=max_final, items=build_candidate_block(items))

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": float(llm_cfg.get("temperature", 0.2)),
        "max_tokens": int(llm_cfg.get("max_tokens", 2000)),
        "stream": False,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    url = base_url.rstrip("/") + "/chat/completions"
    log(f"Calling DeepSeek with {len(items)} candidates...")
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=180)
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"].strip()
        log("DeepSeek returned successfully")
        return content
    except Exception as exc:
        log(f"DeepSeek call failed, fallback to rule digest: {exc}")
        return None


def build_fallback_report(items: list, cfg: dict) -> str:
    if not items:
        return "今日没有发现符合关键词的新内容。"
    lines = [f"# {cfg.get('digest_name', '每日情报')}\n", f"生成时间：{datetime.now():%Y-%m-%d %H:%M}\n"]
    for i, item in enumerate(items[: int(cfg.get("max_items_final", 12))], 1):
        date_str = item.get("date").strftime("%Y-%m-%d") if item.get("date") else ""
        lines.append(f"### {i}. [{item.get('source')}] {item.get('title')}")
        if date_str:
            lines.append(f"日期：{date_str}")
        summary = clean_html(item.get("summary", ""))
        if summary:
            lines.append(f"摘要：{summary[:300]}")
        lines.append(f"链接：{item.get('url')}")
        lines.append("")
    return "\n".join(lines)


def build_report(items: list, cfg: dict, llm_result: Optional[str]) -> str:
    header = f"# {cfg.get('digest_name', '每日情报')}\n\n> 生成时间 {datetime.now():%Y-%m-%d %H:%M}，由 DeepSeek 精筛。\n\n"
    if llm_result:
        return header + llm_result.strip() + "\n"
    return header + build_fallback_report(items, cfg)


def markdown_to_plain(markdown: str) -> str:
    """QQ 不渲染 Markdown，简单转成纯文本再发送。"""
    lines = []
    for line in markdown.splitlines():
        line = re.sub(r"^#{1,6}\s*", "", line)
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        line = re.sub(r"\*(.+?)\*", r"\1", line)
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", line)
        lines.append(line)
    return "\n".join(lines).strip()


def send_wechat(title: str, content: str) -> bool:
    push_type = (
        os.getenv("PUSH_TYPE", "").strip().lower()
        or os.getenv("WECHAT_PUSH_TYPE", "").strip().lower()
        or "none"
    )
    if push_type == "none" or not push_type:
        log("未配置 PUSH_TYPE/WECHAT_PUSH_TYPE；不会标记已读。请用 --dry-run 查看，或设置 serverchan/qmsg/wecom/pushplus")
        return False

    if push_type == "serverchan":
        sendkey = os.getenv("SERVERCHAN_SENDKEY", "").strip()
        if not sendkey:
            log("SERVERCHAN_SENDKEY is empty")
            return False
        url = f"https://sctapi.ftqq.com/{sendkey}.send"
        resp = requests.post(url, data={"title": title, "desp": content}, timeout=30)
        resp.raise_for_status()
        ok = resp.json().get("code") in (0, "0")
        log(f"ServerChan push {'ok' if ok else resp.text[:200]}")
        return ok

    if push_type == "qmsg":
        key = os.getenv("QMSG_KEY", "").strip()
        qq = os.getenv("QMSG_QQ", "").strip()
        if not key:
            log("QMSG_KEY is empty")
            return False
        if not qq:
            log("QMSG_QQ is empty")
            return False
        plain_text = markdown_to_plain(content)
        msg = f"{title}\n\n{plain_text}"[:1000]
        url = f"https://qmsg.zendee.cn/v3/send/{key}"
        data = {"msg": msg, "qq": qq}
        resp = requests.post(url, data=data, timeout=30)
        resp.raise_for_status()
        ok = resp.json().get("success") is True or resp.json().get("code") in (0, "0")
        log(f"Qmsg酱 QQ push {'ok' if ok else resp.text[:200]}")
        return ok


    if push_type == "wecom":
        webhook = os.getenv("WECOM_WEBHOOK_URL", "").strip()
        if not webhook:
            log("WECOM_WEBHOOK_URL is empty")
            return False
        text = content[:3900]
        payload = {"msgtype": "markdown", "markdown": {"content": text}}
        resp = requests.post(webhook, json=payload, timeout=30)
        resp.raise_for_status()
        ok = resp.json().get("errcode") == 0
        log(f"WeCom push {'ok' if ok else resp.text[:200]}")
        return ok

    if push_type == "pushplus":
        token = os.getenv("PUSHPLUS_TOKEN", "").strip()
        if not token:
            log("PUSHPLUS_TOKEN is empty")
            return False
        payload = {"token": token, "title": title, "content": content, "template": "markdown"}
        resp = requests.post("https://www.pushplus.plus/send", json=payload, timeout=30)
        resp.raise_for_status()
        ok = resp.json().get("code") == 200
        log(f"PushPlus push {'ok' if ok else resp.text[:200]}")
        return ok

    log(f"Unsupported PUSH_TYPE: {push_type}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="AI for Biology daily digest")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--state", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true", help="only print, no push, no state update")
    parser.add_argument("--no-llm", action="store_true", help="skip DeepSeek")
    args = parser.parse_args()

    cfg = load_config(args.config)
    state_path = args.state or Path(os.getenv("STATE_FILE", str(DEFAULT_STATE)))
    state = load_state(state_path)
    now = get_now()

    log("Fetching sources...")
    all_items = fetch_all(cfg)
    if not all_items:
        log("No items fetched")
        return 0

    new_items, new_ids = filter_and_dedupe(all_items, cfg, state, now)
    new_items = dedupe_in_memory(new_items)
    new_items = sort_items(new_items)
    log(f"New relevant items after filter/dedupe: {len(new_items)}")

    if not new_items:
        log("No new relevant content, skip today")
        return 0

    llm_result = None
    if not args.no_llm:
        candidates = new_items[: int(cfg.get("max_items_before_llm", 40))]
        llm_result = call_deepseek(cfg, candidates)

    report = build_report(new_items, cfg, llm_result)
    title = f"{cfg.get('digest_name', 'Daily Digest')} {now.strftime('%Y-%m-%d')}"

    if args.dry_run:
        print("\n" + "=" * 70)
        print(report)
        print("=" * 70)
        log("dry-run: no push, no state update")
        return 0

    ok = send_wechat(title, report)
    if not ok:
        log("Push failed, state not updated so it can retry next run")
        return 1

    for sid in new_ids:
        state[sid] = now.isoformat()
    save_state(state_path, state)
    log(f"State updated with {len(new_ids)} ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())
