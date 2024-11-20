from sqlalchemy import Column, Integer

from database import Base


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer, primary_key=True)
