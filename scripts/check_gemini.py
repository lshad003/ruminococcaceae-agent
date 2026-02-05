import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv('configs/api_keys.env')
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

print("Available Gemini models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"  - {model.name}")
