# Contributing

Thanks for your interest in improving this project.

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Workflow

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Validate the Python project with:

```bash
python -m py_compile keepalive.py create_session.py
```

5. Open a pull request with a clear description.

## Security guidance

- Never commit session strings or API secrets.
- Use GitHub Secrets for sensitive values.
- Keep all examples safe and anonymized.
