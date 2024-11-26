from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_session
from app.schemas import GuildCreate
from app.services import GuildService

router = APIRouter(prefix="/guilds")


@router.post("/", response_model=GuildCreate)
async def create_guild(guild: GuildCreate, session: Session = Depends(get_session)):
    service = GuildService(session)
    await service.create_guild(guild)
    return guild


@router.delete("/{guild_id}")
async def delete_guild(guild_id: int, session: Session = Depends(get_session)):
    service = GuildService(session)
    return await service.delete_guild(guild_id)
