"""
Telegram Keep-Alive Script

Sends a periodic message to the user's Saved Messages to keep the
Telegram account active and prevent it from being deleted due to inactivity.

This script is designed to run on GitHub Actions via a scheduled workflow.
Credentials are provided via environment variables (GitHub Secrets).

Optional: Set the KEEPALIVE_MESSAGE environment variable to send a custom message.
If not set, a random fun message will be chosen automatically.
"""

import asyncio
import logging
import os
import random
import sys

from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    AuthKeyUnregisteredError,
    FloodWaitError,
    PhoneNumberInvalidError,
)
from telethon.sessions import StringSession

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

def get_required_env(name: str) -> str:
    """Return a required environment variable or exit with a clear message."""
    value = os.environ.get(name)
    if value is None or value.strip() == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value.strip()


# Read credentials from environment variables (set as GitHub Secrets)
API_ID = int(get_required_env("API_ID"))
API_HASH = get_required_env("API_HASH")
SESSION_STRING = get_required_env("SESSION_STRING")

# Optional custom message(s) (set as KEEPALIVE_MESSAGE secret in GitHub)
# Supports either a single value or multiple values separated by "||".
CUSTOM_MESSAGE_RAW = os.environ.get("KEEPALIVE_MESSAGE", "").strip()

# Random delay (in seconds) before sending the message.
# This makes the activity look more human-like and less like an automated bot.
MIN_DELAY_SECONDS = int(os.environ.get("KEEPALIVE_MIN_DELAY_SECONDS", "5"))
MAX_DELAY_SECONDS = int(os.environ.get("KEEPALIVE_MAX_DELAY_SECONDS", "60"))

# Fun messages — a random one is chosen each time unless a custom message is set
FUN_MESSAGES = [
    "👋 Hey there! Just checking in to keep this account alive and kicking!",
    "🔋 Keep-alive ping! Your Telegram is still breathing. You're welcome!",
    "💪 Still here! This account is too awesome to get deleted!",
    "🕐 Weekly check-in! Rumor has it: this account is immortal now.",
    "🚀 Powering up this account so it never disappears. No big deal.",
    "😄 Friendly neighborhood ping! Just making sure you don't get deleted.",
    "🤖 Beep boop. Keeping things alive. Proceed with your day, human.",
    "📡 Signal check: This account is alive, well, and very active. Promise!",
    "🎉 365 days of activity? No. But this ping keeps us in the game!",
    "🛡️ Your account protection squad strikes again. All clear!",
    "⚡ Zap! A weekly spark to keep this account charged up.",
    "🌱 Watering this account like a plant so it never wilts away.",
    "🧟 Plot twist: This account refuses to die. Weekly check complete!",
    "🐢 Slow and steady wins the race. Weekly ping delivered!",
    "🔑 Unlocking the secret to never getting deleted: weekly pings!",
]

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def get_message() -> str:
    """
    Return the message to send.

    Returns:
        A custom message if configured, otherwise a random fun message.
        Multiple custom messages can be provided as a "||"-separated list.
    """
    if CUSTOM_MESSAGE_RAW:
        options = [part.strip() for part in CUSTOM_MESSAGE_RAW.split("||") if part.strip()]
        if options:
            return random.choice(options)

    return random.choice(FUN_MESSAGES)


async def send_keepalive_message() -> None:
    """
    Connect to Telegram and send a keep-alive message to Saved Messages.

    Raises:
        SystemExit: If the session is not authorized or credentials are invalid.
    """
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

    try:
        await client.connect()
        logger.info("Connected to Telegram")

        if not await client.is_user_authorized():
            logger.error("Session is not authorized. Check your SESSION_STRING secret.")
            sys.exit(1)

        me = await client.get_me()
        logger.info("Connected as: %s (@%s)", me.first_name, me.username)

        # Random delay to appear more human-like
        delay = random.randint(MIN_DELAY_SECONDS, MAX_DELAY_SECONDS)
        logger.info("Waiting %d seconds before sending...", delay)
        await asyncio.sleep(delay)

        message = get_message()
        await client.send_message("me", message)
        logger.info("Keep-alive message sent to Saved Messages: %s", message)

    except ApiIdInvalidError:
        logger.error("Invalid API ID or API HASH. Check your secrets.")
        sys.exit(1)
    except AuthKeyUnregisteredError:
        logger.error("Session key is no longer valid. Generate a new SESSION_STRING.")
        sys.exit(1)
    except PhoneNumberInvalidError:
        logger.error("Phone number associated with the session is invalid.")
        sys.exit(1)
    except FloodWaitError as e:
        logger.error("Rate limited by Telegram. Try again in %d seconds.", e.seconds)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001 - catch-all for unexpected errors
        logger.error("Unexpected error: %s", e)
        sys.exit(1)
    finally:
        await client.disconnect()
        logger.info("Disconnected from Telegram")


async def main() -> None:
    """Entry point: send the keep-alive message."""
    await send_keepalive_message()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(0)