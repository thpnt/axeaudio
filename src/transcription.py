from config import DATA_DIRECTORY, TRANSCRIPT_DIRECTORY, EDITED_DIRECTORY
from prompt import prompt_article, prompt_cdc
from utils import get_most_recent_file, store_transcript, get_completion
from dotenv import load_dotenv
import openai
import os


#OpenAI creds
_  = load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organizations = "org-cMwR4RMO7oQ1BYbT8J6l48ai"

#Get the audio most recent_audio files in the data_directory
#cwd = os.getcwd()
#PATH = os.path.abspath(os.path.join(cwd, os.pardir))
PATH = os.getcwd()
file_name = get_most_recent_file(DATA_DIRECTORY)
audio_file = open(f"{PATH}/{file_name}", 'rb')


#Transcript audio_file
transcript = openai.Audio.transcribe("whisper-1", audio_file)
text = transcript['text']
#Store raw_transcript
store_transcript(text, TRANSCRIPT_DIRECTORY, DATA_DIRECTORY)


#Text transformation with GPT
treatment_type = input('You want to transcribe a web articles ? ("y" if True else "n" then type enter) : ')

while not any(treatment_type == x for x in ['y', 'n']) :
    treatment_type = input('Invalid input. Enter <y> for web article treatment, <n> for CDC treatment : ')
    
    
match treatment_type:
    case 'y' :
        prompt = prompt_article(text)
        response = get_completion(prompt)
    case 'n' :
        prompt = prompt_cdc(text)
        response = get_completion(prompt)

store_transcript(response, EDITED_DIRECTORY, DATA_DIRECTORY)

        
