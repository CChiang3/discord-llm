from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_session
from app.services import MessageService

router = APIRouter(prefix="/messages", tags=["messages"])


class MessageCreate(BaseModel):
    message_id: int
    guild_id: int
    content: str
    timestamp: datetime


@router.post("/")
async def create_message(message: MessageCreate, session: Session = Depends(get_session)):
    service = MessageService(session)
    return await service.create_message(
        message.message_id, message.guild_id, message.content, message.timestamp
    )


@router.get("/{message_id}")
async def get_message(message_id: int, session: Session = Depends(get_session)):
    service = MessageService(session)
    return await service.get_message(message_id)


@router.delete("/{message_id}")
async def delete_message(message_id: int, session: Session = Depends(get_session)):
    service = MessageService(session)
    return await service.delete_message(message_id)
