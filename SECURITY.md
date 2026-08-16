# Security notice

This project stores sensitive Telegram credentials in GitHub repository secrets and uses a session string that grants access to a Telegram account.

## Do not commit these values

Never commit or upload the following files or values:

- `session.txt`
- `*.session`
- `*.session-journal`
- API credentials, API IDs, API HASH values
- Session strings
- Telegram account login data

## Recommended setup

1. Generate the session string only on your local machine.
2. Save it only in a local environment or GitHub repository secret.
3. Ensure `.gitignore` excludes session files.
4. Never print or paste the session string into public issues, pull requests, chats, or logs.

## Risk acknowledgement

This project may interact with Telegram in a way that could trigger automated-activity detection, rate limits, or account restrictions. Use it at your own risk and only after understanding the implications.

## Reporting a security issue

If you discover a sensitive issue in the project, contact the repository maintainer privately and do not disclose the issue publicly before a fix is ready.
