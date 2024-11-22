# Standalone Audio ML Application

The **Standalone Audio ML Application** is an innovative tool that integrates multiple machine learning models to create a complete audio processing pipeline. It includes **Automatic Speech Recognition (ASR)** to transcribe audio, **Natural Language Processing (NLP)** to analyze the sentiment of the transcribed text, and **Text-to-Speech (TTS)** to generate a spoken response based on the sentiment. This project showcases the potential of combining these technologies for interactive and personalized audio-based applications.

This repository contains a Python-based implementation that allows users to either record audio through a microphone or process pre-recorded audio files. The application processes the audio in three stages:
1. **Transcription**: The audio is transcribed into text using a Wav2Vec2 ASR model.
2. **Sentiment Analysis**: The transcribed text is analyzed for sentiment using a fine-tuned DistilBERT model.
3. **Response Generation**: Based on the sentiment analysis, a predefined response is generated.
4. **Speech Synthesis**: The response text is then converted into speech using a Tacotron2-based TTS model.

Additionally, a simple graphical user interface (GUI) built with Tkinter is included to allow users to easily interact with the application. This makes it accessible for users who prefer not to use the command line interface.

## Features

- **Automatic Speech Recognition (ASR)**: 
  - Uses the Wav2Vec2 model from Hugging Face to transcribe speech into text with high accuracy.
  - Capable of transcribing audio files with a sample rate of 16kHz.
  
- **Sentiment Analysis (NLP)**:
  - Uses the pre-trained DistilBERT model fine-tuned on the SST-2 dataset for sentiment classification (positive, negative, or neutral).
  - Analyzes the transcribed text and categorizes it into one of the three sentiment classes.
  
- **Text-to-Speech (TTS)**:
  - Converts the generated response text into natural-sounding speech using the Tacotron2 model.
  - Generates a `.wav` file that can be played back to the user.
  
- **Audio Acquisition**:
  - Records audio directly from the microphone using the `sounddevice` library.
  - Option to record audio for a specified duration or process pre-recorded audio files.
  
- **Graphical User Interface (GUI)**:
  - Built using `Tkinter`, the GUI provides an easy-to-use interface for interacting with the application.
  - Features buttons for recording audio, processing audio files, and quitting the application.

## Files

### `asr.py`
This script contains the `ASRModel` class which initializes and uses the Wav2Vec2 model from Hugging Face to perform Automatic Speech Recognition. It includes a method `transcribe` that takes an audio file and returns the transcribed text.

### `nlp.py`
The `SentimentAnalyzer` class in this script uses a fine-tuned DistilBERT model for sentiment analysis. It includes an `analyze` method that accepts text input and returns the sentiment of the text (positive, negative, or neutral).

### `tts_module.py`
Contains the `TTSModel` class which interacts with the Tacotron2-based TTS model. It includes a `synthesize` method that converts a given text into speech and saves it as a `.wav` file.

### `audio_acquisition.py`
This script provides functions for recording and loading audio. The `record_audio` function records audio for a specified duration, while the `load_audio` function loads an audio file and ensures it has the correct sample rate.

### `main.py`
The main script that handles the overall audio processing pipeline. It provides functionality for both command-line and GUI usage:
- If using the command line, it allows the user to record or select an audio file, process it through the ASR, NLP, and TTS stages, and generate a response.
- The script also handles cleanup of temporary files after processing.

### `gui_app.py`
A simple Tkinter-based GUI for interacting with the application. Users can record audio or select an audio file to process. The results, including the transcription, sentiment analysis, and response text, are displayed in the GUI.

## Installation

To set up the **Standalone Audio ML Application** on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/standalone-audio-ml-app.git
   cd standalone-audio-ml-app
