import unittest
from unittest.mock import patch
from clients.GeminiKit import GeminiBot
from clients.GeminiKit import VALID_MODELS as VALID_GEMINI_MODELS
from clients.OpenAIKit import OpenAIBot
from clients.OpenAIKit import VALID_MODELS as VALID_OPENAI_MODELS
import google.generativeai as genai

MOCK_RESPONSE: str = "This is a mock response for test purposes"  # use MOCK_COMPLETION?


class TestGeminiBot(unittest.TestCase):
    # unittest.TestCase is a class whose instances are single test cases.
    def setUp(self) -> None:  # a hook method for setting up the test fixture before exercising it. # fmt: skip
        # return super().setUp() # default return statement
        self.bot = GeminiBot()

    def test_valid_model(self):
        for model in VALID_GEMINI_MODELS:
            bot = GeminiBot(model=model)
            self.assertIsInstance(bot.model, genai.GenerativeModel)
            # self.assertEqual(bot.model.model_name.split("/")[-1], model)  # Check model name after instantiation # fmt: skip
            self.assertIn(member=bot.model.model_name.replace("models/", ""), container=VALID_GEMINI_MODELS)  # fmt: skip

    # @patch("google.generativeai.GenerativeModel.generate_content")
    # def create_completion_test(self, generate_content_mock):
    #     generate_content_mock.return_value = genai.types.Generation(text=MOCK_RESPONSE)
    #     completion = self.bot.create_completion(prompt="Who are the Beastie Boys?")
    #     response = completion.text
    #     self.assertEqual(type(response), type(MOCK_RESPONSE))


if __name__ == "__main__":
    unittest.main()
