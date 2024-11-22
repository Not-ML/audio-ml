# gui_app.py
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from asr import ASRModel
from nlp import SentimentAnalyzer
from tts_module import TTSModel
from audio_acquisition import record_audio, load_audio
import os
import simpleaudio as sa

class AudioMLApp:
    def __init__(self, master):
        self.master = master
        master.title("Standalone Audio ML Application")

        # Setup models
        self.asr = ASRModel()
        self.nlp = SentimentAnalyzer()
        self.tts = TTSModel()

        self.record_button = tk.Button(master, text="Record Audio", command=self.record_audio)
        self.record_button.pack()

        self.process_button = tk.Button(master, text="Process Audio File", command=self.process_audio_file)
        self.process_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def record_audio(self):
        threading.Thread(target=self._record_audio).start()

    def _record_audio(self):
        input_audio = "input.wav"
        record_audio(duration=5, output_path=input_audio)
        self.process_audio_pipeline(input_audio)

    def process_audio_file(self):
        file_path = filedialog.askopenfilename(title="Select Audio File")
        if file_path:
            self.process_audio_pipeline(file_path)

    def process_audio_pipeline(self, input_audio_path):
        transcription = self.asr.transcribe(input_audio_path)
        sentiment = self.nlp.analyze(transcription)
        response_text = "I'm sorry to hear that." if sentiment[0]['label'] == 'NEGATIVE' else "Glad you're feeling positive!"

        output_audio_path = "response.wav"
        self.tts.synthesize(response_text, output_audio_path)

        # Play generated audio
        wave_obj = sa.WaveObject.from_wave_file(output_audio_path)
        wave_obj.play()
        
        messagebox.showinfo("Processing Complete", f"Transcription: {transcription}\nResponse: {response_text}")

# Main function to launch GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AudioMLApp(root)
    root.mainloop()
