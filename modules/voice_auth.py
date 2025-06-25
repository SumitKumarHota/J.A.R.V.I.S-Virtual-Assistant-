import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
from numpy import dot
from numpy.linalg import norm
import os
from scipy.io.wavfile import write
import sounddevice as sd

from modules.speech_engine import speak
from modules import user_data

# ✅ Load the model ONCE at the top – this is the fix
encoder = VoiceEncoder()

def record_input_for_auth():
    duration = 4
    fs = 44100
    speak("Voice sample detected")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write("input.wav", fs, recording)
    print("Voice input recorded as input.wav")

def extract_features(file_path):
    try:
        wav = preprocess_wav(file_path)
        return encoder.embed_utterance(wav)
    except Exception as e:
        print(f"Resemblyzer feature extraction failed: {e}")
        return None

def authenticate_user():
    input_features = extract_features("input.wav")
    if input_features is None:
        speak("Could not process your voice.")
        return False

    voice_folder = "voice_profiles"
    threshold = 0.50

    best_match = None
    best_score = 0

    for file in os.listdir(voice_folder):
        if file.endswith(".wav"):
            profile_path = os.path.join(voice_folder, file)
            profile_features = extract_features(profile_path)
            if profile_features is None:
                continue

            score = dot(input_features, profile_features) / (norm(input_features) * norm(profile_features))
            print(f"Match score with {file}: {score}")

            if score > best_score and score >= threshold:
                best_score = score
                best_match = file

    # Clean up input.wav
    try:
        os.remove("input.wav")
        print("Cleaned up input.wav")
    except Exception as e:
        print(f"Failed to delete input.wav: {e}")

    if best_match:
        user_data.name = os.path.splitext(best_match)[0].strip()
        speak("Voice recognized. Access granted")
        return True
    else:
        return False
