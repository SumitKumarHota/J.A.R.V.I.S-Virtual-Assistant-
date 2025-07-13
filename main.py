import os
import sys
import shutil
import warnings
import atexit

from resemblyzer import VoiceEncoder
from modules.speech_engine import speak, setup_engine, is_offline, is_internet, cleanup, takeCommand
from modules.voice_auth import authenticate_user
from modules import user_data  

try:
    atexit.register(cleanup)
    setup_engine()
    is_offline()
    is_internet()

    from modules.command_handler import handle_command, wishMe, birthday

    speak("Importing preferences and calibrating virtual environment. We're online and ready. Greetings. I'm Jarvis, a virtual assistant created by Master Sumit")

    if os.path.exists("input.wav"):
        os.remove("input.wav")

    while True:
        print("Waiting for command...")
        result = takeCommand()  
        
        if not result:
            continue
            
        query, audio_data = result
        query = query.lower() if query else ""
        print(f"Query detected: {query}")

        if "jarvis" in query and audio_data is not None:
            print("Jarvis command recognized.")
            
            # Save the wake word audio for authentication
            with open("input.wav", "wb") as f:
                f.write(audio_data)
            print("Saved wake word audio to input.wav")
            speak("Voice sample detected")
            
            if not authenticate_user():
                speak("Unauthorized voice. Access denied.")
                continue

            wishMe(user_data.name)
            birthday()
            speak("How may I assist you?")
        
            # Inner command loop
            while True:
                print("Waiting for next command...")
                result = takeCommand()
                
                if not result:
                    continue
                    
                inner_query, inner_audio = result  # Use the result we already have
                inner_query = inner_query.lower() if inner_query else ""
                
                if inner_query in ["bye", "sleep", "freeze", "get lost", "going to sleep"]:
                    speak("Initiating sleep mode")
                    break

                elif "going to sleep" in inner_query:
                    speak("Good night. See ya soon")
                    break

                elif "exit" in inner_query or "offline" in inner_query or "standby" in inner_query:
                    speak("It was my pleasure serving you. Goodbye")
                    cleanup()
                    sys.exit()

                else:
                    handle_command(inner_query)

except Exception as e:
    print(f"Critical error: {e}")
    speak("System offline at the moment. Entering standby mode.")
    cleanup()
    sys.exit()
