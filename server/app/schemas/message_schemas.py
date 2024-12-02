from datetime import datetime

from pydantic import BaseModel


class MessageCreate(BaseModel):
    id: int
    guild_id: int
    content: str
    timestamp: datetime
