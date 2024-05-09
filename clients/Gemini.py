import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")


if __name__ == "__main__":
    prompt: str = "What year is it?"
    response = model.generate_content(prompt)
    print(type(response.text))
    print(response.text)  # <class str>
    # print(type(response)) # <class 'google.generativeai.types.generation_types.GenerateContentResponse'>
