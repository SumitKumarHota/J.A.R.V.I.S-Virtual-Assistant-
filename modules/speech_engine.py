import pyttsx3
import speech_recognition as sr
import socket
import time
import atexit

from modules import user_data

engine = pyttsx3.init()

def cleanup():
    print("Cleaning up before exit...")
    engine.stop()

def is_offline():
    try:
        # Get the local IP address (non-loopback indicates active network)
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        # If it's a loopback address, likely no network

        if local_ip.startswith("127."):
            return True  # Offline
        return False     # Connected to some network (not necessarily internet)
    except:
        return True  # Error resolving IP — treat as offline

def setup_engine():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Male voice
    engine.setProperty('rate', 130)  # Natural pace
    engine.setProperty('volume', 1.0)

def speak(*lines):
    try:
        text = " ".join(str(line) for line in lines)
        print(f"Speaking: {text}")

        if user_data.first_speak:
            engine.say("")            # Warm-up (silent)
            engine.runAndWait()
            time.sleep(0.3)
            user_data.first_speak = False
        else:
            time.sleep(0.15)          # Slight pause before speaking

        engine.stop()                 # Clear buffer if stuck
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Speech error: {e}")

def is_internet():
    count = 0
    while True:
        if not is_offline():
            break

        speak("Searching for a valid internet connection...")
        count += 1

        if count == 3:
            break

        time.sleep(5)

def takeCommand():
    r = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)  # To account for ambient noise
                audio = r.listen(source, timeout=15, phrase_time_limit=15)
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-us")
                print(f"Command: {query}")
                return query.lower()

        except sr.WaitTimeoutError:
            print("Timeout Error: No speech detected.")
            continue
        except OSError as e:
            if "Unanticipated host error" in str(e) or "Stream closed" in str(e):
                print("Audio device disconnected or not found. Reinitializing...")
                time.sleep(1)  # Delay before retrying to allow for device reconnection
                continue
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            continue
        except sr.RequestError:
            print("Sorry, the speech service is down.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
