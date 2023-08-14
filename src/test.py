from dotenv import load_dotenv
import os
_ = load_dotenv()
print(os.getenv('OPENAI_API_KEY'))