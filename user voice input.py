import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_user_voice():
    # Ask for user's name
    name = input("Enter your name: ").strip()

    if not name:
        print("Invalid name. Try again.")
        return

    # Create profiles directory if not exists
    os.makedirs("voice_profiles", exist_ok=True)

    # Set filename
    filename = os.path.join("voice_profiles", f"{name}.wav")

    # Recording settings
    duration = 4  # seconds
    fs = 44100    # sample rate

    print(f"\nRecording voice for {name}... Speak clearly.")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)

    print(f"\nVoice profile saved as: {filename}")

if __name__ == "__main__":
    record_user_voice()
