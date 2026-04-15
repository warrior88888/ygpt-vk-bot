from pydantic import BaseModel, PositiveInt


class ContextConfig(BaseModel):
    max_messages: PositiveInt = 3
    ttl: PositiveInt = 3600
