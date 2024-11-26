from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.database import Base, get_engine
from app.graphql import schema
from app.models import Guild, Message  # noqa: F401

engine = get_engine()
Base.metadata.create_all(bind=engine)

graphql = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
