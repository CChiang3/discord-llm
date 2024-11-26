from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.database.session import get_session
from app.schemas import GuildCreate
from app.services import GuildService

router = APIRouter(prefix="/guilds")


@router.post("/", response_model=GuildCreate)
async def create_guild(
    guild: GuildCreate, response: Response, session: Session = Depends(get_session)
):
    service = GuildService(session)

    try:
        await service.create_guild(guild)
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return

    response.status_code = status.HTTP_201_CREATED
    return guild


@router.delete("/{guild_id}")
async def delete_guild(guild_id: int, response: Response, session: Session = Depends(get_session)):
    service = GuildService(session)

    try:
        await service.delete_guild(guild_id)
    except Exception:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return

    response.status_code = status.HTTP_204_NO_CONTENT
    return
