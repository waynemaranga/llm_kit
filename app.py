from clients.GeminiKit import GeminiBot
from clients.OpenAIKit import OpenAIBot

gemini_test = GeminiBot()  # using default model i.e "gemini-1.5-pro-latest"
gpt_4_test = OpenAIBot(model="gpt-4")  # specifying model (default is "gpt-3.5-turbo")

if __name__ == "__main__":

    print(f"{gpt_4_test.create_completion(prompt="Who were the Beastie Boys?")}")
    print(f"{gemini_test.create_completion(prompt="Who are the Beastie Boys?")}")
