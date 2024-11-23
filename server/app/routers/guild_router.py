from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.session import get_session
from app.services import GuildService

router = APIRouter(prefix="/guilds", tags=["guilds"])


class GuildCreate(BaseModel):
    guild_id: int


@router.post("/")
async def create_guild(guild: GuildCreate, session: Session = Depends(get_session)):
    service = GuildService(session)
    return await service.create_guild(guild.guild_id)


@router.get("/{guild_id}")
async def get_guild(guild_id: int, session: Session = Depends(get_session)):
    service = GuildService(session)
    return await service.get_guild(guild_id)


@router.delete("/{guild_id}")
async def delete_guild(guild_id: int, session: Session = Depends(get_session)):
    service = GuildService(session)
    return await service.delete_guild(guild_id)
