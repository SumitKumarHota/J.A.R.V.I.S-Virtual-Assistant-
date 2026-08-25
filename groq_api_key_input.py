"""
groq_api_key_input.py

Standalone, double-clickable script — no dependency on the rest of the
Jarvis codebase. Run it once to enter your free Groq API key
(get one at https://console.groq.com/keys). It's saved locally to
config/groq_key.txt, where ai_qa.py reads it from automatically.

Double-click this file (or run `python groq_api_key_input.py`) to use it.
"""

import os

CONFIG_DIR = "config"
KEY_FILE = os.path.join(CONFIG_DIR, "groq_key.txt")


def main():
    print("=" * 50)
    print(" Groq API Key Setup")
    print("=" * 50)
    print("Get a free key here: https://console.groq.com/keys\n")

    existing = ""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            existing = f.read().strip()

    if existing:
        masked = existing[:4] + "..." + existing[-4:] if len(existing) > 8 else "****"
        print(f"A key is already saved ({masked}).")
        choice = input("Replace it with a new key? (y/n): ").strip().lower()
        if choice != "y":
            print("Keeping existing key. Nothing changed.")
            input("\nPress Enter to exit...")
            return

    key = input("Paste your Groq API key: ").strip()

    if not key:
        print("No key entered. Nothing was saved.")
        input("\nPress Enter to exit...")
        return

    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(KEY_FILE, "w") as f:
        f.write(key)

    print(f"\nKey saved to {KEY_FILE}")
    print("You can now use the AI Q&A feature (run ai_qa.py or use it from Jarvis).")
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
