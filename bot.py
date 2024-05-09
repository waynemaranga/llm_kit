from clients import Client


class Bot:
    def __init__(self, bot_name: str, client: Client) -> None:
        self.bot_name = bot_name
        self.client_name = client.name

    def __str__(self) -> str:
        return f"{self.bot_name} [{self.client_name}]"

    def create(self):
        return NotImplemented
