import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY,
)

model = "claude-3-opus-20240229"
max_tokens = 1024

message = client.messages.create(
    model=model,
    max_tokens=max_tokens,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content)
