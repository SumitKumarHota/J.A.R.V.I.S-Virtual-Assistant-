import sounddevice as sd
from scipy.io.wavfile import write
import os
import numpy as np
import time  # Added missing import
from scipy.signal import resample  # Added missing import

def record_user_voice():
    name = input("Enter your name: ").strip()
    if not name:
        print("Invalid name. Try again.")
        return

    os.makedirs("voice_profiles", exist_ok=True)
    filename = os.path.join("voice_profiles", f"{name}.wav")
    
    # Match your microphone's specifications
    fs = 48000  # 48kHz sampling rate
    channels = 2  # Stereo recording
    duration = 4  # 4 seconds
    
    print(f"\nRecording voice for {name}... Say 'Jarvis' clearly at normal volume.")
    print("Recording starts in 2 seconds...")
    time.sleep(2)
    
    # Record with hardware-native format
    recording = sd.rec(int(duration * fs), 
                       samplerate=fs, 
                       channels=channels,
                       dtype='int16')
    
    # Wait for recording to complete
    sd.wait()
    
    # Convert to mono by averaging channels
    if channels > 1:
        mono_recording = np.mean(recording, axis=1).astype(np.float32)
    else:
        mono_recording = recording.flatten().astype(np.float32)
    
    # Normalize volume - handle zero division
    max_val = np.max(np.abs(mono_recording))
    if max_val > 0:
        mono_recording /= max_val
    
    # Resample to 16kHz for Resemblyzer compatibility
    target_fs = 16000  # Required sample rate
    num_samples = int(len(mono_recording) * target_fs / fs)  # Fixed calculation
    resampled = resample(mono_recording, num_samples)
    
    # Convert to 16-bit PCM and save
    int16_data = (resampled * 32767).astype(np.int16)
    write(filename, target_fs, int16_data)
    
    print(f"Voice profile saved: {filename}")
    print(f"Format: {target_fs}Hz, mono, 16-bit PCM")

if __name__ == "__main__":
    record_user_voice()
