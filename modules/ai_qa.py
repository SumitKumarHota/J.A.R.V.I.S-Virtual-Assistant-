"""
modules/ai_qa.py

Groq-powered fallback for questions that don't match any predefined
command in command_handler.py. Reads the API key the user saved via
groq_api_key_input.py (config/groq_key.txt) — this module does not
ask for input itself, it only consumes the key.

If no key has been saved yet, ask_ai() speaks a short reminder and
returns, so it never crashes the assistant.
"""

import os
from modules.speech_engine import speak

KEY_FILE = os.path.join("config", "groq_key.txt")
MODEL = "openai/gpt-oss-120b"

_client = None
_warned_missing_key = False


def _load_key():
    if not os.path.exists(KEY_FILE):
        return None
    with open(KEY_FILE, "r") as f:
        key = f.read().strip()
    return key or None


def _get_client():
    global _client
    if _client is not None:
        return _client

    try:
        from groq import Groq
    except ImportError:
        print("The 'groq' package isn't installed. Run: pip install groq")
        return None

    api_key = _load_key()
    if not api_key:
        return None

    _client = Groq(api_key=api_key)
    return _client


def ask_ai(question):
    """Send an unmatched question to Groq and speak back a short answer."""
    global _warned_missing_key

    client = _get_client()
    if client is None:
        if not _warned_missing_key:
            speak("I don't have a Groq API key set up yet. Run groq_api_key_input.py to add one.")
            _warned_missing_key = True
        else:
            print("No Groq API key configured. Run groq_api_key_input.py.")
        return

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are JARVIS, a concise voice assistant. "
                        "Answer in 1-3 short spoken sentences, plain text only, "
                        "since this will be read aloud."
                    ),
                },
                {"role": "user", "content": question},
            ],
            temperature=0.6,
            max_tokens=200,
        )
        answer = response.choices[0].message.content.strip()
        print(f"AI answer: {answer}")
        speak(answer)
    except Exception as e:
        print(f"Groq API error: {e}")
        speak("Sorry, I couldn't reach my AI brain right now.")
