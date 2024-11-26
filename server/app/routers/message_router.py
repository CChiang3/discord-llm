from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_session
from app.schemas import MessageCreate
from app.services import MessageService

router = APIRouter(prefix="/messages")


@router.post("/", response_model=MessageCreate)
async def create_message(message: MessageCreate, session: Session = Depends(get_session)):
    service = MessageService(session)
    await service.create_message(message)
    return message


@router.delete("/{message_id}")
async def delete_message(message_id: int, session: Session = Depends(get_session)):
    service = MessageService(session)
    return await service.delete_message(message_id)
