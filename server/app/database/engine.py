import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

_engine = None


def get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = create_engine(os.getenv("DATABASE_URL"))

    return _engine
