# audio_acquisition.py
import sounddevice as sd
import numpy as np
import librosa
import soundfile as sf

def record_audio(duration=5, sample_rate=16000, output_path="input.wav"):
    print("Recording audio...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    audio = np.squeeze(recording)
    sf.write(output_path, audio, sample_rate)
    print(f"Audio recorded and saved to {output_path}")

def load_audio(file_path, target_sr=16000):
    audio, sr = librosa.load(file_path, sr=target_sr)
    sf.write("temp.wav", audio, target_sr)
    return "temp.wav"
