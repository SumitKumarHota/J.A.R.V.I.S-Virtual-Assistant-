import os
import sys
import shutil
import warnings
import atexit

from resemblyzer import VoiceEncoder
from modules.speech_engine import speak, setup_engine, is_offline, is_internet, cleanup, takeCommand
from modules.voice_auth import record_input_for_auth, authenticate_user
from modules.command_handler import handle_command, wishMe, birthday

from modules import user_data  # <-- NEW

try:
    atexit.register(cleanup)
    setup_engine()
    is_offline()
    is_internet()

    if getattr(sys, 'frozen', False):
    bundled_model_path = os.path.join(sys._MEIPASS, ".resemblyzer", "pretrained.pt")
    target_folder = os.path.join(os.path.expanduser("~"), ".resemblyzer")
    target_model_path = os.path.join(target_folder, "pretrained.pt")
    if not os.path.exists(target_model_path):
        os.makedirs(target_folder, exist_ok=True)
        shutil.copy(bundled_model_path, target_model_path)

    warnings.filterwarnings("ignore", category=FutureWarning)

    speak("Importing preferences and calibrating virtual environment. We're online and ready. Greetings. I'm Jarvis, a virtual assistant created by Master Sumit")

    if os.path.exists("input.wav"):
    os.remove("input.wav")

    while True:
    print("Waiting for command...")
    query = takeCommand().lower()
    print(f"Query detected: {query}")

    if "jarvis" in query:
        print("Jarvis command recognized.")
        record_input_for_auth()

        if not authenticate_user():
            speak("Unauthorized voice. Access denied.")
            continue

        wishMe(user_data.name)
        birthday()
        speak("How may I assist you?")

        while True:
            query = takeCommand().lower()

            if query in ["bye", "sleep", "freeze", "get lost", "going to sleep"]:
                speak("Initiating sleep mode")
                break

            elif "going to sleep" in query:
                speak("Good night. See ya soon")
                break

            elif "exit" in query or "offline" in query or "standby" in query:
                speak("It was my pleasure serving you. Goodbye")
                cleanup()
                sys.exit()

            else:
                handle_command(query)

except Exception:
    speak("System offline at the moment. Entering standby mode.")
    cleanup()
    sys.exit()

