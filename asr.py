# asr.py
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torch
import librosa

class ASRModel:
    def __init__(self, model_name="facebook/wav2vec2-base-960h", device=None):
        self.tokenizer = Wav2Vec2Tokenizer.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def transcribe(self, audio_path):
        speech, sr = librosa.load(audio_path, sr=16000)
        input_values = self.tokenizer(speech, return_tensors="pt", padding="longest").input_values.to(self.device)
        with torch.no_grad():
            logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.tokenizer.decode(predicted_ids[0])
        return transcription.lower()
