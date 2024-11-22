# tts_module.py
from TTS.api import TTS

class TTSModel:
    def __init__(self, model_name="tts_models/en/ljspeech/tacotron2-DDC", gpu=False):
        self.tts = TTS(model_name=model_name, progress_bar=False, gpu=gpu)

    def synthesize(self, text, output_path="output.wav"):
        self.tts.tts_to_file(text=text, file_path=output_path)
