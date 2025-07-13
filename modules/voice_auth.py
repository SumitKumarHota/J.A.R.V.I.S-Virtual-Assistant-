import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
import os
from scipy.io.wavfile import write
import sounddevice as sd
import time  # Missing import for sleep
from scipy.signal import resample, butter, filtfilt  # Missing imports

from modules.speech_engine import speak
from modules import user_data

_encoder = None

def get_encoder():
    global _encoder
    if _encoder is None:
        _encoder = VoiceEncoder()  # Initialize only once
        print("Voice encoder model loaded")
    return _encoder

def extract_features(file_path):
    try:
        encoder = get_encoder()  # MUST GET ENCODER INSTANCE HERE
        
        # Load and preprocess - RESEMBLYZER HANDLES RESAMPLING
        wav = preprocess_wav(file_path)
        
        # Apply audio enhancements
        from resemblyzer.audio import normalize_volume, trim_long_silences
        
        # Normalize volume
        wav = normalize_volume(wav, 30, increase_only=True)
        
        # Trim silences
        wav = trim_long_silences(wav)
        
        # Bandpass filter for voice frequencies
        b, a = butter(4, [300/(16000/2), 3400/(16000/2)], btype='bandpass')
        wav = filtfilt(b, a, wav)
        
        # Generate embedding
        return encoder.embed_utterance(wav)
    except Exception as e:
        print(f"Feature extraction failed: {e}")
        return None

def authenticate_user():
    #Extract features from input
    input_features = extract_features("input.wav")
    if input_features is None:
        speak("Could not process your voice.")
        return False

    voice_folder = "voice_profiles"
    if not os.path.exists(voice_folder):
        speak("No voice profiles found")
        return False

    # Dynamic threshold
    base_threshold = 0.55
    environment_factor = 0.05
    threshold = base_threshold - environment_factor
    
    best_match = None
    best_score = 0
    
    print("\nVoice Authentication Results:")
    print("=" * 60)
    
    # Compare against all profiles
    for file in os.listdir(voice_folder):
        if not file.endswith(".wav"):
            continue
            
        profile_path = os.path.join(voice_folder, file)
        profile_features = extract_features(profile_path)
        
        if profile_features is None:
            print(f"Skipping {file} - feature extraction failed")
            continue
            
        # 1. Cosine similarity
        cos_sim = np.dot(input_features, profile_features)
        
        # 2. Euclidean similarity
        euclidean_dist = np.linalg.norm(input_features - profile_features)
        euclidean_sim = 1 / (1 + euclidean_dist)
        
        # 3. Combined score (weighted average)
        combined_score = 0.7 * cos_sim + 0.3 * euclidean_sim
        
        print(f"{file:<25} Cosine: {cos_sim:.4f}  Euclidean: {euclidean_sim:.4f}  Combined: {combined_score:.4f}")
        
        # Update best match
        if combined_score > best_score and combined_score >= threshold:
            best_score = combined_score
            best_match = file

    print("=" * 60)
    
    # Clean up
    try:
        os.remove("input.wav")
        print("Cleaned up input.wav")
    except Exception as e:
        print(f"Failed to delete input.wav: {e}")
    
    # Handle match results
    if best_match:
        # Clean name from filename
        name = os.path.splitext(best_match)[0]
        name = ''.join([c for c in name if not c.isdigit()]).replace('_', ' ').strip()
        
        user_data.name = name
        print(f"BEST MATCH: {name} with score {best_score:.4f}")
        speak("Voice recognized. Access granted")
        return True
    else:
        if best_score > 0:
            print(f"Best score {best_score:.4f} below threshold {threshold:.4f}")
            speak("Voice not recognized")
        return False
