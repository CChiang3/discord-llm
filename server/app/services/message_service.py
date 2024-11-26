from datetime import datetime

from sqlalchemy.orm import Session

from app.models.message import Message
from app.repositories import GuildRepository, MessageRepository

from .llm_service import LLMService


class MessageService:
    def __init__(self, session: Session):
        self.message_repository = MessageRepository(session)
        self.guild_repository = GuildRepository(session)
        self.llm_service = LLMService()

    async def get_message(self, message_id: int) -> Message:
        message = await self.message_repository.get_message(message_id)
        if message is None:
            raise Exception()

        return message

    async def create_message(
        self, message_id: int, guild_id: int, content: str, timestamp: datetime
    ) -> Message:
        guild = await self.guild_repository.get_guild(guild_id)
        if guild is None:
            raise Exception()

        message = await self.message_repository.get_message(message_id)
        if message is not None:
            raise Exception()

        embedding = await self.llm_service.embed_text(content)

        return await self.message_repository.create_message(
            message_id, guild_id, content, embedding, timestamp
        )

    async def delete_message(self, message_id: int) -> bool:
        message = await self.message_repository.get_message(message_id)
        if message is None:
            raise Exception()

        success = await self.message_repository.delete_message(message_id)
        if not success:
            raise Exception()

        return True
