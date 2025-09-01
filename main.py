from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Carica le variabili da .env
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("La variabile d'ambiente OPENAI_API_KEY non è impostata.")

openai.api_key = api_key

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
