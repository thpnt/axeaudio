from config import DATA_DIRECTORY
from utils import get_most_recent_file
import openai
import os


#OpenAI creds
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organizations = "org-cMwR4RMO7oQ1BYbT8J6l48ai"


#Get the audio most recent_audio files in the data_directory
cwd = os.getcwd()
PATH = os.path.abspath(os.path.join(cwd, os.pardir))
file_name = get_most_recent_file(DATA_DIRECTORY)
audio_file = open(f"{PATH}/{DATA_DIRECTORY}/{file_name}")


#Transcript audio_file
transcript = openai.Audio.transcribe("whisper-1", audio_file)

def store_raw_transcript(content, filename):
    with open(filename, 'w') as file:
        file.write(content)