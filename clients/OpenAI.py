import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)
system_role = ""
prompt = "What year is it?"

# fmt: off
completion = client.chat.completions.create(
    model="gpt-4", 
    messages=[
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt}
        ]
    )
# fmt: on

if __name__ == "__main__":
    prompt: str = "What year is it?"
    response = completion.choices[0].message.content
    print(response)  # <class str>
    print(type(completion))  # <class 'openai.types.chat.chat_completion.ChatCompletion'> # fmt: skip
