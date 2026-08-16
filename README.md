# 📱 Telegram Keep-Alive

[![Workflow Status](https://img.shields.io/github/actions/workflow/status/daniel-malka-148/telegram-keepalive/keepalive.yml)](https://github.com/daniel-malka-148/telegram-keepalive/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Keep your Telegram account alive.** A free, automated GitHub Actions workflow that sends a message to your Saved Messages every week.

---

## ⚡ How it works

```
GitHub Schedule ──▶ GitHub Actions ──▶ keepalive.py ──▶ Telegram Saved Messages
```

1. GitHub Actions runs the workflow **every Sunday at 10:00 UTC** (or manually).
2. The script connects to Telegram using your credentials.
3. It sends a short message to your own **Saved Messages**.
4. Your account stays active — no more risk of deletion.

---

## 🚀 Setup

### 1. Create a session string

Run this once on your computer:

```bash
pip install -r requirements.txt
python create_session.py
```

The script will ask for your API credentials (from [my.telegram.org](https://my.telegram.org)), phone number, and verification code. It saves the session string to `session.txt`.

> ⚠️ **The session string is a password to your account. Never share it, never commit it.**

### 2. Add GitHub secrets

In your repository, go to **Settings → Secrets and variables → Actions** and add:

| Secret | Description |
|---|---|
| `API_ID` | Your Telegram API ID |
| `API_HASH` | Your Telegram API HASH |
| `SESSION_STRING` | The session string from step 1 |

### 3. Run the workflow

Trigger it manually once to test:

1. Open the **Actions** tab
2. Select **Telegram Keep-Alive**
3. Click **Run workflow** → **Run workflow**
4. Check the logs — it should complete in ~1 minute ✅

After that, it runs automatically every Sunday.

---

## 🎨 Customization

All settings are optional.

| Secret | What it does | Example |
|---|---|---|
| `KEEPALIVE_MESSAGE` | Custom message(s). Use `\|\|` for multiple. | `"Still alive \|\| Weekly ping"` |
| `KEEPALIVE_MIN_DELAY_SECONDS` | Min random delay before sending | `5` |
| `KEEPALIVE_MAX_DELAY_SECONDS` | Max random delay before sending | `60` |

**Schedule:** edit the `cron` line in [`.github/workflows/keepalive.yml`](.github/workflows/keepalive.yml).

---

## 📁 Structure

```
├── .github/workflows/keepalive.yml   # GitHub Actions workflow
├── keepalive.py                      # Main script
├── create_session.py                 # One-time session generator
├── requirements.txt                  # Dependencies
├── .gitignore                        # Protects session.txt 🔒
└── LICENSE                           # MIT
```

---

## ❓ FAQ

**Is it free?** Yes — GitHub Actions free tier covers this easily.

**Is it safe?** It sends one message per week to your own Saved Messages. That said, automated activity may violate Telegram's ToS — use at your own risk.

**The workflow failed. What now?** Open the run logs. Most common cause: wrong `SESSION_STRING` or missing secrets.

---

## ⚠️ Disclaimer

This project uses [Telethon](https://github.com/LonamiWebs/Telethon) and automates account activity. Telegram may restrict accounts showing automated behavior. **Use at your own risk.**

---

## 📄 License

MIT — see [LICENSE](LICENSE).

---

## 🌐 Languages

- [English](README.md) · [עברית](README.he.md)

<div align="center">Made with ❤️ by <a href="https://github.com/daniel-malka-148">Daniel Malka</a></div>