import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

basic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
model = "claude-3-opus-20240229"
max_tokens = 1024

completion = basic_client.messages.create(
    model=model,
    max_tokens=max_tokens,
    messages=[{"role": "user", "content": "Hello, world"}],
)

stream_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

with stream_client.messages.stream(
    max_tokens=max_tokens,
    messages=[{"role": "user", "content": "Hello"}],
    model=model,
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
