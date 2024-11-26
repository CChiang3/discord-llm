import os
from typing import List

from ollama import Client


class LLMService:
    def __init__(self):
        self.model = os.getenv("OLLAMA_MODEL")
        self.client = Client(host=os.getenv("OLLAMA_URL"))

    async def generate_text(self, prompt: str) -> str:
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
        )

        return response.response

    async def embed_text(self, text: str) -> List[float]:
        response = self.client.embed(
            model=self.model,
            input=text,
        )

        return response.embeddings[0]

    async def embed_texts(self, texts: List[str]) -> List[List[float]]:
        response = self.client.embed(
            model=self.model,
            input=texts,
        )

        return response.embeddings
