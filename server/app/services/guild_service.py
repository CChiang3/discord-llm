from sqlalchemy.orm import Session

from app.models.guild import Guild
from app.repositories import GuildRepository


class GuildService:
    def __init__(self, session: Session):
        self.guild_repository = GuildRepository(session)

    async def get_guild(self, guild_id: int) -> Guild:
        guild = await self.guild_repository.get_guild(guild_id)
        if guild is None:
            raise Exception()

        return guild

    async def create_guild(self, guild_id: int) -> Guild:
        guild = await self.guild_repository.create_guild(guild_id)
        if guild is not None:
            raise Exception()

        return await self.guild_repository.create(guild_id)

    async def delete_guild(self, guild_id: int) -> bool:
        success = await self.guild_repository.delete_guild(guild_id)
        if not success:
            raise Exception()

        return True
