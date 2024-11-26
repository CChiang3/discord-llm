from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.database.session import get_session
from app.schemas import MessageCreate
from app.services import MessageService

router = APIRouter(prefix="/messages")


@router.post("/", response_model=MessageCreate)
async def create_message(
    message: MessageCreate, response: Response, session: Session = Depends(get_session)
):
    service = MessageService(session)
    try:
        await service.create_message(message)
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        print("erro")
        return

    response.status_code = status.HTTP_201_CREATED
    return message


@router.delete("/{message_id}")
async def delete_message(
    message_id: int, response: Response, session: Session = Depends(get_session)
):
    service = MessageService(session)
    try:
        await service.delete_message(message_id)
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return

    response.status_code = status.HTTP_204_NO_CONTENT
    return
