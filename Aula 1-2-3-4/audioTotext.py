import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
# Initialize the Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# Specify the path to the audio file
filename = os.path.dirname(__file__) + "/audio.mp3" # Replace with your audio file!

# Open the audio file
with open(filename, "rb") as file:
    # Create a transcription of the audio file
    transcription = client.audio.transcriptions.create(
      file=file, # Required audio file
      model="whisper-large-v3-turbo", # Required model to use for transcription
    )
    # To print only the transcription text, you'd use print(transcription.text) (here we're printing the entire transcription object to access timestamps)
    print(json.dumps(transcription, indent=2, default=str))