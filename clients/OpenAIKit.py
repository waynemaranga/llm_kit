import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-3.5-turbo"
VALID_MODELS: list[str] = []
DEFAULT_MAX_TOKENS = 1024
DEFAULT_TEMPERATURE = 0.5
DEFAULT_SYSTEM_MESSAGE = "Your a helpful chatbot"  # Cannot be empty

client = OpenAI(api_key=OPENAI_API_KEY)


class OpenAIBot:
    def __init__(
        self, model=None, max_tokens=None, temperature=None, system_message=None
    ):
        self.model = DEFAULT_MODEL or model  # TODO: Error handling if model passed isn't in list of valid models # fmt: skip
        # self.name = f"OpenAI: {model[0]}"
        self.max_tokens = DEFAULT_MAX_TOKENS or max_tokens
        self.temperature = DEFAULT_TEMPERATURE or temperature
        self.system_message = DEFAULT_SYSTEM_MESSAGE or system_message

    def __str__(self) -> str:
        # return self.name
        return NotImplementedError

    def create_completion(self, prompt: str, assistant: str = None) -> str:
        DEFAULT_ASSISTANT: str = "Send a clear and concise answer"
        completion = client.chat.completions.create(
            max_tokens=self.max_tokens,
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": DEFAULT_ASSISTANT or assistant},
            ],
        )

        return completion.choices[0].message.content


if __name__ == "__main__":
    test_bot = OpenAIBot()
    print(test_bot.create_completion(prompt="Who is Kenya's first president?"))
