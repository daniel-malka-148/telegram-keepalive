# 📱 Telegram Keep-Alive

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/daniel-malka-148/telegram-keepalive/keepalive.yml)](https://github.com/daniel-malka-148/telegram-keepalive/actions)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com)

> Keep your Telegram account active by sending a short, natural-looking message to your own Saved Messages.

This project is a lightweight GitHub Actions automation that helps keep a Telegram account from appearing inactive. It is designed to be simple, transparent, and easy to run without a complicated interface.

This is a CLI-based automation project rather than a full app, and that is intentional: the real value is in its simplicity, reliability, and easy setup process.

---

## ✨ Why this project is useful

- Runs for free on GitHub Actions
- Fully automated after setup
- Lightweight and easy to understand
- Easy to fork and customize
- Minimal dependencies and a clean workflow

---

## ⚠️ Before you start

This project uses your Telegram API credentials and session string. Those values are sensitive and should be handled like passwords.

- Never upload `session.txt` or any Telegram session file to GitHub
- Keep credentials in GitHub Secrets only
- Do not share your API hash or session string with anyone
- Use this project at your own risk
- Telegram may restrict or disable accounts that show unusual automated behavior

---

## 🧭 Quick start checklist

Use this workflow in order:

1. Download or clone the repository
2. Install the Python dependency
3. Create a Telegram session string locally
4. Add API credentials and session string as GitHub secrets
5. Trigger the workflow once to validate it
6. Let GitHub Actions handle it automatically from then on

---

## 🧠 How it works

```text
GitHub schedule
    ↓
GitHub Actions
    ↓
keepalive.py
    ↓
Telegram API
    ↓
Saved Messages
```

1. GitHub Actions runs the workflow on a schedule or manually.
2. The workflow installs the required Python packages.
3. The script connects to Telegram using your API credentials and session string.
4. It waits a random short delay and sends a message to your own Saved Messages.
5. The account remains active and avoids looking abandoned.

---

## 🚀 Features

- ✅ Free GitHub-hosted automation
- ✅ Weekly or custom cron scheduling
- ✅ Randomized delay before sending
- ✅ Random message selection from a built-in list
- ✅ Support for custom messages via secret
- ✅ Very small project footprint and easy onboarding

---

## 📦 Prerequisites

Before you get started, make sure you have:

1. A Telegram account
2. API credentials from [my.telegram.org](https://my.telegram.org)
   - `api_id`
   - `api_hash`
3. Python 3.12+
4. A GitHub account

---

## 🛠 Quick start

### Step 1: Create a session string

Run this once on your local machine:

```bash
pip install -r requirements.txt
python create_session.py
```

The script will ask for:

1. API ID
2. API HASH
3. Phone number with country code
4. Telegram verification code
5. 2FA password if enabled

At the end, it will print the session string and save it to `session.txt`.

> The session string is a real credential. Keep it private.

### Step 2: Clone or fork the repository

```bash
git clone https://github.com/YOUR_USERNAME/telegram-keepalive.git
cd telegram-keepalive
```

### Step 3: Add your GitHub secrets

Go to:

Settings → Secrets and variables → Actions → New repository secret

Add the following:

| Secret name | Value |
|---|---|
| `API_ID` | Your Telegram API ID |
| `API_HASH` | Your Telegram API HASH |
| `SESSION_STRING` | The session string created in Step 1 |

Optional values:

| Secret name | Value |
|---|---|
| `KEEPALIVE_MESSAGE` | Message text or multiple values separated by `||` |
| `KEEPALIVE_MIN_DELAY_SECONDS` | Minimum delay before sending, for example `5` |
| `KEEPALIVE_MAX_DELAY_SECONDS` | Maximum delay before sending, for example `60` |

### Step 4: Run the workflow

The workflow is already configured in `.github/workflows/keepalive.yml`.

You can either:

- wait for the scheduled job to run, or
- trigger it manually in the GitHub Actions tab

For a quick test:

1. Open the repository on GitHub
2. Go to the Actions tab
3. Select Telegram Keep-Alive
4. Click Run workflow
5. Check the logs after a few minutes

---

## 🎯 Customization ideas

### Randomized messages

You can set a random pool of messages by using `||` separators:

```bash
KEEPALIVE_MESSAGE="Checking in || Still active || Weekly ping || All good here"
```

If the secret is not set, the script picks one message from the built-in list automatically.

### Less predictable scheduling

Instead of a fixed weekly run, you can change the cron expression in `.github/workflows/keepalive.yml`.

Example:

```yaml
- cron: "0 6,12,18 * * *"
```

This creates a more natural-looking pattern than a single rigid schedule.

### Random delay

You can tune the action timing with:

```bash
KEEPALIVE_MIN_DELAY_SECONDS=5
KEEPALIVE_MAX_DELAY_SECONDS=60
```

This makes each run feel less robotic.

---

## 📁 Project structure

```text
telegram-keepalive/
├── .github/
│   └── workflows/
│       └── keepalive.yml
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── README.he.md
├── SECURITY.md
├── .env.example
├── create_session.py
├── keepalive.py
├── requirements.txt
├── session.txt
└── telegram-keepalive/
    └── keepalive.py
```

---

## ❓ FAQ

### Is it really free?
Yes. GitHub Actions is often sufficient for this kind of lightweight workflow.

### Is it safe?
This script sends a real message to your own private Saved Messages. It is not a spam bot and does not contact random users. However, Telegram may still detect unusual automation patterns.

### What if the workflow fails?
Open the failing run in the Actions tab and inspect the logs. The most common cause is an invalid session string or missing secret.

### Can I modify the schedule?
Yes. Edit the cron expression in `.github/workflows/keepalive.yml`.

### Can I customize the message pool?
Yes. Use the `KEEPALIVE_MESSAGE` secret with multiple values separated by `||`.

---

## 🔐 Security

This project keeps secrets out of source control and expects them to live in GitHub secrets instead.

Recommended practices:

- Never commit your session string
- Keep `.env` files private
- Do not expose secrets in logs or issues
- Rotate or regenerate the session if you suspect it has been exposed

See [SECURITY.md](SECURITY.md) for the security policy.

---

## ⚠️ Disclaimer

Use this project at your own risk.

- It relies on the Telethon library to communicate with the Telegram API
- Automated account activity may violate Telegram terms or trigger restrictions
- The author is not responsible for any consequences arising from the use of this software
- The project is provided as-is, without any warranty

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🌐 Languages

- [English](README.md)
- [עברית](README.he.md)

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/daniel-malka-148">Daniel Malka</a>
</div>