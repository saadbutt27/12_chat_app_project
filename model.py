from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from typing import Any
from openai.types.chat.chat_completion import ChatCompletion

class MyAIBot:
    def __init__(self, name:str, model:str = "gpt-3.5-turbo-1106") -> None:
        self.name: str = name
        self.model: str = model
        load_dotenv(find_dotenv())
        self.client: OpenAI = OpenAI()
        self.messages: list[dict[str, str]] = []

    def load_chat_history(self) -> list[dict[str, str]]:
        return self.messages

    def save_chat_history(self, message: dict[str, str])-> None:
        # print("Model: Save", self.messages)
        self.messages.append(message)

    def get_messages(self)->list[dict[str, str]]:
        return self.messages
    
    def send_message(self, message:dict[str,str]) -> ChatCompletion:
        # Add user message to chat history
        self.save_chat_history(message)
        response: ChatCompletion = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True
        )
        return response
