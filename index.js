require('dotenv').config();
const mic = require('mic');
const fs = require('fs');
const axios = require('axios');
const say = require('say');

// Configuration
const MIC_DURATION = 5; // seconds
const AUDIO_FILE = 'input.wav';
const RESPONSE_AUDIO = 'response.wav';

// Initialize microphone
const microphone = mic({
    rate: '16000',
    channels: '1',
    debug: false,
    device: 'default',
    exitOnSilence: 6
});
const micInputStream = microphone.getAudioStream();
const outputFileStream = fs.WriteStream(AUDIO_FILE);

console.log("Recording...");

micInputStream.pipe(outputFileStream);

microphone.start();

setTimeout(() => {
    microphone.stop();
}, MIC_DURATION * 1000);

// After recording
micInputStream.on('end', async () => {
    console.log("Recording stopped. Processing...");

    try {
        // ASR: Send audio to external API (e.g., AssemblyAI)
        const transcript = await transcribeAudio(AUDIO_FILE);
        console.log(`Transcribed Text: ${transcript}`);

        // NLP: Simple sentiment analysis placeholder
        const sentiment = await analyzeSentiment(transcript);
        console.log(`Sentiment: ${sentiment}`);

        // Generate response
        let responseText = "";
        if (sentiment === 'positive') {
            responseText = "I'm glad you're feeling good today!";
        } else {
            responseText = "I'm sorry to hear that. How can I assist you?";
        }

        console.log(`Response Text: ${responseText}`);

        // TTS: Generate audio response
        say.export(responseText, null, 1, RESPONSE_AUDIO, (err) => {
            if (err) {
                return console.error(err);
            }
            console.log(`Generated audio saved at: ${RESPONSE_AUDIO}`);
        });

    } catch (error) {
        console.error(error);
    }
});

// Function to transcribe audio using AssemblyAI
async function transcribeAudio(filePath) {
    const apiKey = process.env.ASSEMBLYAI_API_KEY;
    if (!apiKey) throw new Error("Missing ASSEMBLYAI_API_KEY in .env");

    // Upload audio
    const uploadResponse = await axios({
        method: 'post',
        url: 'https://api.assemblyai.com/v2/upload',
        headers: {
            authorization: apiKey,
            'Content-Type': 'application/octet-stream'
        },
        data: fs.readFileSync(filePath)
    });
    const audioUrl = uploadResponse.data.upload_url;

    // Request transcription
    const transcriptResponse = await axios({
        method: 'post',
        url: 'https://api.assemblyai.com/v2/transcript',
        headers: { authorization: apiKey, 'Content-Type': 'application/json' },
        data: { audio_url: audioUrl }
    });
    const transcriptId = transcriptResponse.data.id;

    // Poll for transcription completion
    let transcript = '';
    while (true) {
        const pollingResponse = await axios({
            method: 'get',
            url: `https://api.assemblyai.com/v2/transcript/${transcriptId}`,
            headers: { authorization: apiKey }
        });
        if (pollingResponse.data.status === 'completed') {
            transcript = pollingResponse.data.text;
            break;
        } else if (pollingResponse.data.status === 'error') {
            throw new Error("Transcription failed.");
        }
        await new Promise(resolve => setTimeout(resolve, 3000)); // Wait 3 seconds
    }
    return transcript;
}

// Function to analyze sentiment (placeholder using simple keywords)
async function analyzeSentiment(text) {
    const positiveKeywords = ['good', 'happy', 'fantastic', 'great', 'awesome'];
    const negativeKeywords = ['bad', 'sad', 'terrible', 'horrible', 'worst'];

    const textLower = text.toLowerCase();
    for (let word of positiveKeywords) {
        if (textLower.includes(word)) return 'positive';
    }
    for (let word of negativeKeywords) {
        if (textLower.includes(word)) return 'negative';
    }
    return 'neutral';
}
