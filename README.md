# AI x Bio Daily Research Digest Agent

每天自动从 **arXiv + Nature Machine Intelligence + Nature Computational Science + Nature/Science/Cell (CNS) 正刊** 抓取与
**AI for Biology / 蛋白质 / 多肽 / 大语言模型 / 生成模型** 相关的新论文与新闻，由 **DeepSeek** 精筛和点评后，推送到你的 **微信 / QQ**。

整个流程跑在 **GitHub Actions** 云上，你的电脑不需要开机。

---

## 功能

- 定时每天一次（默认北京 09:00，可在 workflow 中修改）
- 多源抓取：arXiv API + RSS
- 关键词规则第一轮过滤
- DeepSeek 第二轮智能精筛/排序/一句话点评
- 推送：支持 QQ Qmsg酱 / Server酱 / 企业微信群机器人 / PushPlus
- 已推送记录自动去重，不会每天重复推同样内容
- 开源友好：Secrets 全部走 GitHub Secrets，不把 Key 写进仓库

---

## 目录结构

```text
.
├── app.py                  # 主程序
├── config.yaml             # 关键词、来源、DeepSeek 提示词配置
├── requirements.txt
├── .env.example            # 本地环境变量示例
├── .github/workflows/daily-digest.yml
├── state.json              # 已推送 URL 的去重状态（自动更新，可提交）
└── README.md
```

---

## 需要准备的东西

1. **DeepSeek API Key**（可选但强烈推荐）
   - 到 https://platform.deepseek.com 获取
   - 注意：不要把真实 Key 写进代码或公开仓库

2. **推送渠道**（选一个）

   | 方式 | 适合 | 需要什么 |
   |---|---|---|
   | Qmsg酱（推荐 QQ） | QQ 收消息 | 到 https://qmsg.zendee.cn 用 QQ 登录，获得 Key，并填你的 QQ 号 |
   | Server酱 | 微信收消息 | 到 https://sct.ftqq.com 用 GitHub 登录后获得 SendKey |
   | 企业微信群机器人 | 企业微信群 | 创建企业微信 -> 添加群机器人 -> 得到 Webhook URL |
   | PushPlus | 微信/其他 | http://www.pushplus.plus 获取 token |

   > 如果你不想注册微信，直接选 **Qmsg酱**，用 QQ 就能每天收到汇总。

---

## 部署到 GitHub（推荐，电脑可关机）

假设你的 GitHub 用户名是 `yimingdongdong`，仓库名 `paper_server`。

### 1. 在 GitHub 建仓库并上传

如果你已经装了 GitHub CLI：

```bash
cd ai-bio-daily-digest
gh repo create yimingdongdong/paper_server --public --source=. --remote=origin --push
```

或者手动：

```bash
cd ai-bio-daily-digest
git init
git add .
git commit -m "init: AI for Biology daily digest agent"
git branch -M main
git remote add origin git@github.com:yimingdongdong/paper_server.git
git push -u origin main
```

### 2. 添加 GitHub Secrets

打开仓库：
`https://github.com/yimingdongdong/paper_server/settings/secrets/actions`

添加以下 Secrets（按你选定的推送方式）：

| Secret | 值 | 必填 |
|---|---|---|
| `DEEPSEEK_API_KEY` | 你的 DeepSeek API Key | 推荐 |
| `DEEPSEEK_MODEL` | 例如 `deepseek-chat` | 可选 |
| `PUSH_TYPE` | `qmsg` / `serverchan` / `wecom` / `pushplus` | 必填 |
| `QMSG_KEY` | Qmsg酱 Key | 若用 QQ Qmsg酱 |
| `QMSG_QQ` | 接收消息的 QQ 号 | 若用 QQ Qmsg酱 |
| `SERVERCHAN_SENDKEY` | Server酱 SendKey | 若用 Server酱 |
| `WECOM_WEBHOOK_URL` | 企业微信群机器人 Webhook | 若用企业微信 |
| `PUSHPLUS_TOKEN` | PushPlus Token | 若用 PushPlus |

> 旧版本用的 `WECHAT_PUSH_TYPE` 仍然兼容，但建议统一使用 `PUSH_TYPE`。

### 3. 手动触发一次验证

打开仓库 `Actions` 页 -> 选择 **Daily AI Bio Digest** -> 点 **Run workflow**，等跑完看微信/QQ 是否收到。

### 4. 之后自动运行

工作流已配置 `cron: "0 1 * * *"`，即 UTC 01:00 / 北京 09:00 自动执行。

---

## 本地测试

```bash
cp .env.example .env
# 编辑 .env，填入 DeepSeek / Qmsg酱 或你选择的推送配置
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 只打印不推送（不会标记已读）
python app.py --dry-run

# 正常推送
python app.py
```

---

## 常见问题

### 1. 某个 RSS 源失败会影响整个任务吗？
不会。程序对每个源单独 try/catch，失败会打印日志并继续其他源。

### 2. 为什么我收到了重复？
如果上一次推送失败，状态不会记录，下次会重试。另外 `state.json` 需要在 GitHub Actions 中成功 commit 才会跨天生效。

### 3. 怎么用 QQ 接收？
1. 打开 https://qmsg.zendee.cn ，用 QQ 登录
2. 获取你的 Qmsg酱 Key
3. 在 GitHub Secrets 里设置：
   - `PUSH_TYPE=qmsg`
   - `QMSG_KEY=你的 Key`
   - `QMSG_QQ=接收消息的QQ号`
4. 手动触发一次 Actions 验证


### 4. X/Twitter 和微信公众号能加吗？
可以，但建议先跑通现在的 RSS/arXiv 版本。
- X：可通过官方 API v2 或 RSSHub 转 RSS。
- 微信公众号：可通过 RSSHub / 搜狗微信等，但稳定性一般。
在 `config.yaml` 的 `sources` 里加一条 `type: rss` 的 URL 即可，例如：

```yaml
- name: "某公众号 via RSSHub"
  type: rss
  url: "https://rsshub.app/wechat/..."
```

### 5. 想改推送时间？
编辑 `.github/workflows/daily-digest.yml` 中的 cron，注意 GitHub Actions 使用 UTC 时间。

### 6. 我的 DeepSeek Key 已经写在聊天里了，安全吗？
建议尽快到 DeepSeek 后台删除/重置该 Key。本项目所有代码都从环境变量/Secret 读取，不会把真实 Key 提交到仓库。

---

## License

MIT
