# ygpt-vk-bot

A VK chatbot for English learning powered by Yandex GPT. Maintains per-user conversation context, enforces rate limits, and deploys via Docker.

## Features

- Conversational English tutoring with Yandex GPT
- Per-user dialog history stored in Redis (configurable depth and TTL)
- Rate limiting and duplicate-request protection
- Graceful shutdown on `SIGTERM` (Docker-safe)
- CI/CD via GitHub Actions: lint → build → deploy → Telegram notify

## Commands

| Command | Description |
|---|---|
| `/start` (payload) | Welcome message |
| `/info` | Help and usage guide |
| `/clear` | Reset conversation history |

## Stack

- **Runtime** — Python 3.13, [vkbottle](https://github.com/vkbottle/vkbottle), [Yandex AI Studio SDK](https://github.com/yandex-cloud/yandex-ai-studio-python)
- **Cache** — Redis 7 (context, throttling, processing state)
- **Config** — pydantic-settings, `.env` with `BOT__` prefix
- **Tooling** — uv, ruff, ty, Docker, GitHub Actions

## Quick start

```bash
cp .env.example .env
# fill in the required values

docker compose up -d
```

## Configuration

All settings use the `BOT__` prefix and `__` as the nested delimiter.

| Variable | Required | Default | Description |
|---|---|---|---|
| `BOT__VK__API_KEY` | yes | — | VK community API token |
| `BOT__YANDEX__API_KEY` | yes | — | Yandex Cloud API key |
| `BOT__YANDEX__FOLDER_ID` | yes | — | Yandex Cloud folder ID |
| `BOT__YANDEX__MODEL_URI` | yes | — | Model URI (e.g. `gpt://<folder>/yandexgpt/latest`) |
| `BOT__YANDEX__TEMPERATURE` | yes | — | Sampling temperature (0.0 – 1.0) |
| `BOT__YANDEX__MAX_TOKENS` | yes | — | Max tokens per response |
| `BOT__REDIS__PASSWORD` | yes | — | Redis password |
| `BOT__REDIS__PORT` | yes | — | Redis port |
| `BOT__REDIS__HOST` | no | `localhost` | Set to `redis` in Docker (done automatically) |
| `BOT__LOG__LEVEL` | no | `INFO` | Log level (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |
| `BOT__CONTEXT__MAX_MESSAGES` | no | `3` | Message pairs kept in history |
| `BOT__CONTEXT__TTL` | no | `3600` | Context TTL in seconds |
| `BOT__RATE_LIMITS__LIMIT` | no | `100` | Max messages per window |
| `BOT__RATE_LIMITS__WINDOW` | no | `60` | Rate limit window in seconds |
| `BOT__RATE_LIMITS__PROCESSING_TTL` | no | `20` | Max seconds a request stays "in progress" |

## CI/CD

Push to `main` triggers:

1. **Lint** — `ruff` + `ty`
2. **Build & push** — Docker image to DockerHub
3. **Deploy** — SSH into VPS, write `.env`, pull and restart containers
4. **Notify** — Telegram message on success or failure

Required GitHub secrets: `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `HOST`, `USER`, `SSH_KEY`, `PASSPHRASE`, `PORT`, all `BOT__*` variables, `TELEGRAM_TO`, `TELEGRAM_TOKEN`.
