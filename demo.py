import assemblyai as aai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("Assembly_AI_KEY")

aai.settings.api_key = API_KEY

# audio_file = "./local_file.mp3"
audio_file = open("Assm.mp3", "rb")

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)