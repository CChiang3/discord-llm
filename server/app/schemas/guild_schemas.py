from pydantic import BaseModel


class GuildCreate(BaseModel):
    id: int
