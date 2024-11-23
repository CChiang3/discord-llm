from typing import List, Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.models.guild import Guild


class GuildRepository:
    def __init__(self, session: Session):
        self.session = session

    async def all(self) -> List[Guild]:
        return list(self.session.query(Guild).all())

    async def get_guild(self, guild_id: int) -> Optional[Guild]:
        try:
            return await self.session.query(Guild).filter(Guild.id == guild_id).one()
        except NoResultFound:
            return None

    async def create_guild(self, guild_id: int) -> Guild:
        guild = Guild(
            id=guild_id,
        )

        self.session.add(guild)
        self.session.commit()
        self.session.refresh(guild)
        return guild

    async def delete_guild(self, guild_id: int) -> bool:
        guild = self.get(guild_id)
        if guild is None:
            return False

        self.session.delete(guild)
        self.session.commit()
        return True
