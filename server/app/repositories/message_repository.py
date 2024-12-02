from datetime import datetime
from typing import List, Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.models.message import Message


class MessageRepository:
    def __init__(self, session: Session):
        self.session = session

    async def all(self) -> List[Message]:
        return list(self.session.query(Message).all())

    async def get_message(self, message_id: int) -> Optional[Message]:
        try:
            return self.session.query(Message).filter(Message.id == message_id).one()
        except NoResultFound:
            return None

    async def get_messages_by_guild_id(self, guild_id: int) -> List[Message]:
        return list(self.session.query(Message).filter(Message.guild_id == guild_id).all())

    async def get_messages_by_similarity(
        self, embedding: List[float], limit: int = 5
    ) -> List[Message]:
        return list(
            self.session.query(Message)
            .order_by(Message.embedding.cosine_distance(embedding))
            .limit(limit)
            .all()
        )

    async def create_message(
        self,
        message_id: int,
        guild_id: int,
        content: str,
        embedding: List[float],
        timestamp: datetime,
    ) -> Message:
        message = Message(
            id=message_id,
            guild_id=guild_id,
            content=content,
            embedding=embedding,
            timestamp=timestamp,
        )

        self.session.add(message)
        self.session.commit()
        self.session.refresh(message)
        return message

    async def update_message(
        self, message_id: int, content: str, embedding: List[float], timestamp: datetime
    ) -> Optional[Message]:
        message = await self.get_message(message_id)
        if message is None:
            return None

        message.content = content
        message.timestamp = timestamp
        message.embedding = embedding
        self.session.commit()
        self.session.refresh(message)
        return message

    async def delete_message(self, message_id: int) -> bool:
        message = await self.get_message(message_id)
        self.session.delete(message)
        self.session.commit()
        return True
