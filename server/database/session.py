import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))

Base = declarative_base()

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with Session() as session:
        yield session
