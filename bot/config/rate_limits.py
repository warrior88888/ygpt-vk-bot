from pydantic import BaseModel, PositiveInt


class RateLimitsConfig(BaseModel):
    limit: PositiveInt = 100
    window: PositiveInt = 60
    processing_ttl: PositiveInt = 20
