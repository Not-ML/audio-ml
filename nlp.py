# nlp.py
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.pipeline = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, text):
        return self.pipeline(text)
