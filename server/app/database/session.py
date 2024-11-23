from typing import Generator

from sqlalchemy.orm import Session, sessionmaker

from .engine import get_engine

_sessionmaker = None


def get_session() -> Generator[Session, None, None]:
    global _sessionmaker
    if _sessionmaker is None:
        engine = get_engine()
        _sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with _sessionmaker() as session:
        yield session
