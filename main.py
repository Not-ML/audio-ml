# main.py
import os
import argparse
from asr import ASRModel
from nlp import SentimentAnalyzer
from tts_module import TTSModel
from audio_acquisition import record_audio, load_audio
from termcolor import colored

def process_audio_pipeline(input_audio_path, asr, nlp, tts):
    # ASR: Transcribe audio to text
    transcription = asr.transcribe(input_audio_path)
    print(colored(f"Transcribed Text: {transcription}", "green"))

    # NLP: Analyze sentiment
    sentiment = nlp.analyze(transcription)
    print(colored(f"Sentiment Analysis: {sentiment}", "yellow"))

    # Generate response based on sentiment
    if sentiment[0]['label'] == 'POSITIVE':
        response_text = "I'm glad you're feeling good today!"
    else:
        response_text = "I'm sorry to hear that. How can I assist you?"

    print(colored(f"Response Text: {response_text}", "cyan"))

    # TTS: Synthesize response
    output_audio_path = "response.wav"
    tts.synthesize(response_text, output_audio_path)
    print(colored(f"Generated audio saved at: {output_audio_path}", "magenta"))

def main():
    parser = argparse.ArgumentParser(description="Standalone Audio ML Application")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--record', action='store_true', help='Record audio from microphone')
    group.add_argument('--file', type=str, help='Path to audio file to process')
    args = parser.parse_args()

    # Initialize models
    print(colored("Initializing ASR Model...", "blue"))
    asr = ASRModel()
    print(colored("Initializing NLP Model...", "blue"))
    nlp = SentimentAnalyzer()
    print(colored("Initializing TTS Model...", "blue"))
    tts = TTSModel()

    # Handle audio input
    if args.record:
        input_audio = "input.wav"
        record_audio(duration=5, output_path=input_audio)
    else:
        input_audio = load_audio(args.file)

    # Process the audio pipeline
    process_audio_pipeline(input_audio, asr, nlp, tts)

    # Cleanup temporary files if any
    if args.file:
        os.remove("temp.wav")

if __name__ == "__main__":
    main()
