# Standalone Audio ML Application

This project is a comprehensive standalone audio machine learning application that integrates multiple technologies to process audio input. It combines Automatic Speech Recognition (ASR), Sentiment Analysis (NLP), and Text-to-Speech (TTS) models, allowing users to interact with audio in an intelligent manner. The application offers a range of functionalities for recording, transcribing, analyzing, and responding to audio in real-time. It also supports both a command-line interface and a GUI for ease of use.

## Features

- **ASR (Automatic Speech Recognition):** Convert spoken words into text using the Wav2Vec2 model by Facebook.
- **Sentiment Analysis:** Analyze the sentiment of the transcribed text using a pre-trained DistilBERT model.
- **TTS (Text-to-Speech):** Generate a spoken response based on the sentiment of the transcription using a Tacotron2-based model.
- **Audio Recording & Processing:** Record audio via the microphone or process pre-recorded audio files.
- **User Interaction:** Respond to the user's emotional tone (positive/negative) with an appropriate message.
- **GUI Application:** Provides a user-friendly interface to record and process audio files with real-time feedback.

## Components

- **asr.py:** Implements the ASR system using the Wav2Vec2 model for speech-to-text conversion.
- **nlp.py:** Uses a pre-trained sentiment analysis pipeline to classify the sentiment of the transcribed text.
- **tts_module.py:** Uses the Tacotron2-based TTS model to synthesize audio responses.
- **audio_acquisition.py:** Handles the recording of audio from the microphone and loading of audio files.
- **main.py:** Integrates all components and runs the audio processing pipeline.
- **gui_app.py:** Provides a graphical interface for users to interact with the application.

## Requirements

- Python 3.x
- transformers, librosa, torch, sounddevice, soundfile, simpleaudio, termcolor, tkinter (for GUI app)
- To run the program, ensure you have the necessary model weights downloaded via HuggingFace or similar sources.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/standalone-audio-ml-app.git
    cd standalone-audio-ml-app
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application (CLI version):

    ```bash
    python main.py --record
    # OR
    python main.py --file <path_to_audio_file>
    ```

4. For GUI version:

    ```bash
    python gui_app.py
    ```

## Configuration

- **ASR Model:** Uses the `facebook/wav2vec2-base-960h` model for speech recognition.
- **NLP Model:** Uses the `distilbert-base-uncased-finetuned-sst-2-english` model for sentiment analysis.
- **TTS Model:** Uses the `tts_models/en/ljspeech/tacotron2-DDC` for text-to-speech synthesis.

## Contributions

Feel free to contribute by forking the repository, creating a branch, and submitting a pull request.

## License

[Insert your license here]
