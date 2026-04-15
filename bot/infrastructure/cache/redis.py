from redis.asyncio import Redis
from redis.backoff import ExponentialBackoff
from redis.exceptions import ConnectionError, TimeoutError
from redis.retry import Retry

from bot.config.settings import settings

_retry = Retry(ExponentialBackoff(cap=8, base=0.5), retries=3)

redis_client = Redis.from_url(
    settings.redis.url,
    decode_responses=True,
    retry=_retry,
    retry_on_error=[ConnectionError, TimeoutError],
    socket_keepalive=True,
    health_check_interval=30,
)
