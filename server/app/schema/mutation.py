import strawberry


@strawberry.type
class Mutation:
    @strawberry.field
    def ping(self) -> str:
        return "pong"
