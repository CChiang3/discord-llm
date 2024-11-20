from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    guild = Column(Integer, ForeignKey("guilds.id"))
    content = Column(String)
    embedding = Column(Vector(4096))
    timestamp = Column(DateTime)
