from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

audio_file_path = "../datasets/audio_files/harvard.wav"

client = OpenAI()

with open(audio_file_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file
    )

print(transcription)