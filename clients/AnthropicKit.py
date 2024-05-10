import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DEFAULT_MODEL = "claude-3-opus-20240229"
VALID_MODELS: list[str] = []
DEFAULT_MAX_TOKENS = 100
DEFAULT_TEMPERATURE = 0.5

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


class AnthropicBot:
    def __init__(self, model=None, max_tokens=None, temperature=None):
        self.model = DEFAULT_MODEL or model
        # self.name = f"Anthropic.{model[0]}"
        self.max_tokens = DEFAULT_MAX_TOKENS or max_tokens
        self.temperature = DEFAULT_TEMPERATURE or temperature

    def __str__(self) -> str:
        # return self.name
        return NotImplementedError

    def create_completion(self, prompt: str) -> str:
        response = client.completions.create(
            # max_tokens=self.max_tokens,
            max_tokens_to_sample=self.max_tokens,
            model=self.model,
            prompt=prompt,
            temperature=self.temperature,
        )

        return response


if __name__ == "__main__":
    test_bot = AnthropicBot()
    print(test_bot.create_completion(prompt="Who is Kenya's first president?"))
