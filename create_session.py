"""
Telegram Keep-Alive - Session Creator

A guided interactive script that generates a Telegram session string.
The session string is required to run the keep-alive script on GitHub Actions.

Run this script ONCE on your local machine:
    python create_session.py

The session string will be displayed and saved to session.txt.
WARNING: The session string grants full access to your account. Never share it!
"""

import asyncio
import os
import sys

from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession

# ---------------------------------------------------------------------------
# ANSI colors for nicer terminal output
# ---------------------------------------------------------------------------

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner() -> None:
    """Print the script banner."""
    print(f"\n{CYAN}{BOLD}{'=' * 50}")
    print("  Telegram Keep-Alive - Session Creator")
    print(f"{'=' * 50}{RESET}\n")


def get_api_credentials() -> tuple[int, str]:
    """
    Prompt the user for their Telegram API ID and API HASH.

    Returns:
        A tuple of (api_id, api_hash).
    """
    while True:
        try:
            api_id_input = input(f"{YELLOW}Enter your API ID (number): {RESET}").strip()
            if not api_id_input.isdigit():
                print(f"{RED}[!] API ID must be a number. Try again.{RESET}")
                continue
            api_id = int(api_id_input)
            break
        except (KeyboardInterrupt, EOFError):
            print(f"\n{RED}[!] Cancelled.{RESET}")
            sys.exit(1)

    api_hash = input(f"{YELLOW}Enter your API HASH: {RESET}").strip()
    if not api_hash:
        print(f"{RED}[!] API HASH cannot be empty.{RESET}")
        sys.exit(1)

    return api_id, api_hash


async def main() -> None:
    """Run the interactive session creation flow."""
    print_banner()

    print(f"{CYAN}[i] You can get your API ID and API HASH from:{RESET}")
    print(f"{CYAN}    https://my.telegram.org -> API development tools{RESET}\n")

    api_id, api_hash = get_api_credentials()

    print(f"\n{GREEN}[+] Connecting to Telegram...{RESET}\n")

    client = TelegramClient(StringSession(), api_id, api_hash)

    try:
        await client.connect()

        # Ask for the phone number and request a verification code
        phone = input(
            f"{YELLOW}Enter your phone number (with country code, e.g. +972...): {RESET}"
        ).strip()
        if not phone:
            print(f"{RED}[!] Phone number cannot be empty.{RESET}")
            sys.exit(1)

        await client.send_code_request(phone)
        print(f"\n{GREEN}[+] Code sent to your Telegram!{RESET}")

        code = input(f"{YELLOW}Enter the code you received: {RESET}").strip()

        try:
            await client.sign_in(phone, code)
        except SessionPasswordNeededError:
            print(f"\n{YELLOW}[!] Two-factor authentication is enabled.{RESET}")
            password = input(f"{YELLOW}Enter your 2FA password: {RESET}")
            await client.sign_in(password=password)
        except PhoneCodeInvalidError:
            print(f"{RED}[!] Invalid code. Please run the script again.{RESET}")
            sys.exit(1)

        me = await client.get_me()
        print(f"\n{GREEN}[+] Logged in as: {BOLD}{me.first_name}{RESET}")

        session_string = client.session.save()

        # Save the session string to a file so it's never lost
        script_dir = os.path.dirname(os.path.abspath(__file__))
        session_file = os.path.join(script_dir, "session.txt")
        with open(session_file, "w", encoding="utf-8") as f:
            f.write(session_string)

        print(f"\n{CYAN}{BOLD}{'=' * 50}")
        print("  YOUR SESSION STRING (KEEP IT SECRET!):")
        print(f"{'=' * 50}{RESET}")
        print(f"\n{GREEN}{BOLD}{session_string}{RESET}\n")
        print(f"{GREEN}[+] Session string also saved to: {BOLD}{session_file}{RESET}")
        print(f"{RED}{BOLD}[!] DO NOT SHARE THIS WITH ANYONE!{RESET}")
        print(f"{RED}[!] This gives full access to your account.{RESET}\n")
        print(f"{CYAN}Copy this string and save it as the SESSION_STRING secret in GitHub.{RESET}\n")

        # Keep the window open so the user can see the output
        input(f"{YELLOW}Press Enter to close...{RESET}")

    except PhoneNumberInvalidError:
        print(f"{RED}[!] Invalid phone number format.{RESET}")
        input(f"{YELLOW}Press Enter to close...{RESET}")
    except ApiIdInvalidError:
        print(f"{RED}[!] Invalid API ID or API HASH.{RESET}")
        input(f"{YELLOW}Press Enter to close...{RESET}")
    except Exception as e:  # noqa: BLE001 - catch-all for unexpected errors
        print(f"{RED}[!] Error: {e}{RESET}")
        input(f"{YELLOW}Press Enter to close...{RESET}")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Cancelled.{RESET}")