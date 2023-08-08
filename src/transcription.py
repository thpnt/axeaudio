from config import DATA_DIRECTORY
import openai
import os


#OpenAI creds
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organizations = "org-cMwR4RMO7oQ1BYbT8J6l48ai"

#Get the audio file 
cwd = os.getcwd()
PATH = os.path.abspath(os.path.join(cwd, os.pardir))
file_name = input("Enter the name of the file to be transcipted : ")
audio_file = open(f"{PATH}/{DATA_DIRECTORY}/{file_name}")


#Transcript audio_file
transcript = openai.Audio.transcribe("whisper-1", audio_file)

def store_raw_transcript(content, filename):
    with open(filename, 'w') as file:
        file.write(content)