import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEFAULT_MODEL = genai.GenerativeModel("gemini-1.5-pro-latest")
VALID_MODELS: list[str] = []
DEFAULT_MAX_TOKENS = 1024
DEFAULT_TEMPERATURE = 0.5
DEFAULT_SYSTEM_MESSAGE = "Your a helpful chatbot"  # Cannot be empty

genai.configure(api_key=GOOGLE_API_KEY)


class GeminiBot:
    def __init__(
        self, model=None, max_tokens=None, temperature=None, system_message=None
    ):
        self.model = DEFAULT_MODEL or genai.GenerativeModel(model)
        self.model = DEFAULT_MODEL or model  # TODO: Error handling if model passed isn't in list of valid models # fmt: skip
        # self.name = f"OpenAI: {model[0]}"
        self.max_tokens = DEFAULT_MAX_TOKENS or max_tokens
        self.temperature = DEFAULT_TEMPERATURE or temperature
        self.system_message = DEFAULT_SYSTEM_MESSAGE or system_message

    def __str__(self) -> str:
        # return self.name
        return NotImplementedError

    def create_completion(self, prompt: str) -> str:
        completion = self.model.generate_content(prompt)
        return completion.text


if __name__ == "__main__":
    test_bot = GeminiBot()
    print(test_bot.create_completion("Who are the Beastie Boys?"))
