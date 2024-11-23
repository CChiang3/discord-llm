from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.database import Base, engine
from app.models import Guild, Message  # noqa: F401
from app.routers import guild_router, message_router
from app.schema import schema

Base.metadata.create_all(bind=engine)

graphql_router = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")
app.include_router(message_router)
app.include_router(guild_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
