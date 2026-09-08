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
import time
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

def extract_authors(entry: Any) -> list:
    authors = []
    for author in entry.get("authors", []):
        if isinstance(author, dict):
            name = str(author.get("name", "") or "").strip()
        else:
            name = str(author).strip()
        if name:
            authors.append(name)
    if not authors and entry.get("author"):
        authors.append(str(entry.get("author")).strip())
    return authors



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
            "authors": extract_authors(entry),
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
            "authors": extract_authors(entry),
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


def is_followed_author(item: dict, cfg: dict) -> bool:
    followed = [str(a).strip().lower() for a in cfg.get("followed_authors", []) if str(a).strip()]
    if not followed:
        return False
    parts = list(item.get("authors", [])) + [item.get("title", ""), item.get("summary", "")]
    haystack = " ".join(parts).lower()
    for name in followed:
        if name in haystack:
            return True
        words = name.split()
        if len(words) > 1 and len(words[-1]) > 3 and words[-1] in haystack:
            return True
    return False


AI_TECH_TERMS = [
    "machine learning", "deep learning", "neural network", "large language model",
    "language model", "llm", "generative", "diffusion", "geometric deep learning",
    "graph neural", "equivariant", "protein language model", "foundation model",
    "drug design", "drug discovery", "molecular generation", "molecular design",
    "ai for drug", "artificial intelligence", "reinforcement learning",
    "representation learning", "self-supervised", "molecular docking",
    "protein design", "peptide design", "antibody design", "virtual screening",
    "de novo", "structure prediction", "alphafold", "geometric", "deep learning",
]

EXPERIMENTAL_TERMS = [
    "clinical trial", "in vivo", "in vitro", "mouse model", "patient",
    "cell line", "breast cancer", "cell cycle", "proteome", "tumor",
    "cancer", "knockout", "mutagenesis", "cryo-em", "x-ray crystallography",
]


def is_technical_ai(item: dict) -> bool:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    return any(term in text for term in AI_TECH_TERMS)


def is_experimental_only(item: dict, cfg: dict) -> bool:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    exp_terms = cfg.get("experimental_terms") or EXPERIMENTAL_TERMS
    if not any(str(t).lower() in text for t in exp_terms):
        return False
    # 只要有 AI/计算/设计相关词，就不当作“纯实验论文”排除
    return not is_technical_ai(item)


def filter_items(all_items: list, cfg: dict, now: datetime) -> list:
    """不做去重、不看历史 state：每次手动/定时执行都会重新发送匹配内容。"""
    selected = []
    for item in all_items:
        if not within_lookback(item, cfg, now):
            continue
        # 关注的研究者：无条件保留
        if is_followed_author(item, cfg):
            selected.append(item)
            continue
        # 纯实验类论文：默认降权/过滤，除非配置 exclude_experimental=false
        if cfg.get("exclude_experimental", True) and is_experimental_only(item, cfg):
            continue
        # 关键词规则
        if cfg.get("use_rule_filter", True) and not rule_relevant(item, cfg):
            continue
        selected.append(item)
    return selected


def sort_items(items: list) -> list:
    def keyfunc(item: dict):
        date = item.get("date")
        if date is None:
            return datetime.min.replace(tzinfo=timezone.utc)
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
        return date
    return sorted(items, key=keyfunc, reverse=True)

def select_llm_candidates(items: list, cfg: dict) -> list:
    """避免 DeepSeek 只看到 arXiv：优先保留非 arXiv 来源，再补 arXiv。"""
    max_n = int(cfg.get("max_items_before_llm", 80))
    non_arxiv = [item for item in items if item.get("source") != "arXiv"]
    arxiv = [item for item in items if item.get("source") == "arXiv"]
    if len(non_arxiv) >= max_n:
        return sort_items(non_arxiv)[:max_n]
    return sort_items(non_arxiv) + sort_items(arxiv)[:max_n - len(non_arxiv)]



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
        authors = ", ".join(item.get("authors", []) or [])
        lines.append(f"<item {idx}>")
        lines.append(f"Source: {item.get('source')}")
        if date_str:
            lines.append(f"Date: {date_str}")
        lines.append(f"Title: {item.get('title')}")
        if authors:
            lines.append(f"Authors: {authors}")
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
    followed = [str(a).strip() for a in cfg.get("followed_authors", []) if str(a).strip()]
    if followed:
        user_prompt = (
            "重点关注以下研究者：如果他们出现在候选中，必须全部保留并优先展示："
            + "、".join(followed)
            + "\n\n"
            + user_prompt
        )

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

def url_to_short_ref(url: str) -> str:
    """把论文 URL 转成 Qmsg 不拦截的短编号/DOI，能不放完整链接就不放。"""
    if not url:
        return ""
    url = url.strip().rstrip(".,;)]}")
    low = url.lower()
    m = None
    if "arxiv.org/abs/" in low or "arxiv.org/pdf/" in low:
        m = re.search(r"(?:abs|pdf)/([0-9]+\.[0-9]+(?:v[0-9]+)?)", url, re.I)
        if m:
            return f"arXiv:{m.group(1)}"
    if "doi.org/" in low:
        doi = url.split("doi.org/", 1)[1].split("?")[0]
        return f"DOI:{doi}"
    if "nature.com/articles/" in low:
        return "Nature ID:" + url.split("/articles/", 1)[1].split("?")[0]
    last = url.rstrip("/").split("/")[-1].split("?")[0]
    if last and len(last) <= 80 and re.fullmatch(r"[A-Za-z0-9._:-]+", last):
        return "ID:" + last
    return ""


def qmsg_plain_text(markdown: str) -> str:
    """Qmsg 会拦截带完整 URL/域名的消息，这里转成纯文本并去掉 URL。"""
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        ref = url_to_short_ref(url)
        return f"{text} ({ref})" if ref else text

    def replace_raw_url(match):
        return url_to_short_ref(match.group(0)) or ""

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, markdown)
    text = re.sub(r"https?://[^\s)]+", replace_raw_url, text)
    text = re.sub(r"www\.[^\s)]+", "", text)
    text = re.sub(r"\b(?:[a-zA-Z0-9-]+\.)+(?:com|org|cn|net|io|edu)(?:/[^\s)]*)?", "", text)
    return markdown_to_plain(text)


def split_qmsg_messages(full_text: str, max_len: int = 1000) -> list:
    """把长文本拆成适合 Qmsg 的多个片段（每条 <= max_len）。"""
    if len(full_text) <= max_len:
        return [full_text]
    lines = full_text.splitlines()
    chunks = []
    current = ""
    for line in lines:
        if not current:
            current = line
            continue
        if len(current) + 1 + len(line) <= max_len:
            current += "\n" + line
        else:
            chunks.append(current)
            # 单行过长时再硬切
            while len(line) > max_len:
                chunks.append(line[:max_len])
                line = line[max_len:]
            current = line
    if current:
        chunks.append(current)
    return chunks


def send_qmsg_text(key: str, qq: str, text: str) -> bool:
    """发送一条 Qmsg 消息，返回是否成功。"""
    url = f"https://qmsg.zendee.cn/v3/send/{key}"
    resp = requests.post(url, data={"msg": text, "qq": qq}, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("success") is True or data.get("code") in (0, "0")



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
        plain_text = qmsg_plain_text(content)
        full_text = f"{title}\n\n{plain_text}"
        messages = split_qmsg_messages(full_text, max_len=1000)
        ok_all = True
        for idx, msg in enumerate(messages, 1):
            # 超过一条时加一个简单序号，避免混淆
            if len(messages) > 1:
                msg = f"[{idx}/{len(messages)}]\n{msg}"[:1000]
            ok = send_qmsg_text(key, qq, msg)
            if not ok:
                ok_all = False
                log(f"Qmsg酱 QQ push failed part {idx}: {msg[:80]}")
                break
            log(f"Qmsg酱 QQ push ok ({idx}/{len(messages)})")
            if idx < len(messages):
                # Qmsg 限流：同一 Key 每 3 秒最多一次
                time.sleep(3.2)
        return ok_all


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
    now = get_now()

    log("Fetching sources...")
    all_items = fetch_all(cfg)
    if not all_items:
        log("No items fetched")
        return 0

    # 不去重、不查历史 state：每次运行都会重新发送符合条件的内容
    new_items = filter_items(all_items, cfg, now)
    new_items = sort_items(new_items)
    log(f"Matching items this run: {len(new_items)}")

    if not new_items:
        log("No matching items in this run, skip sending")
        return 0

    llm_result = None
    if not args.no_llm:
        candidates = select_llm_candidates(new_items, cfg)
        llm_result = call_deepseek(cfg, candidates)

    report = build_report(new_items, cfg, llm_result)
    title = f"{cfg.get('digest_name', 'Daily Digest')} {now.strftime('%Y-%m-%d')}"

    if args.dry_run:
        print("\n" + "=" * 70)
        print(report)
        print("=" * 70)
        log("dry-run: no push")
        return 0

    ok = send_wechat(title, report)
    if not ok:
        log("Push failed")
        return 1

    log("Send completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
