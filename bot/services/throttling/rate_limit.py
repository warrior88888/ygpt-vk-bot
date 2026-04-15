from typing import cast

from bot.config import settings
from bot.infrastructure.cache import CachePrefix, redis_client, redis_safe


def build_key(vk_id: int) -> str:
    return CachePrefix.THROTTLE.key(str(vk_id))


@redis_safe(default=0)
async def set_throttled(vk_id: int) -> int:
    key = build_key(vk_id)
    count = cast(int, await redis_client.incr(key))
    if count == 1:
        # First increment — set expiry. Avoids overwriting TTL on subsequent calls.
        await redis_client.expire(key, settings.rate_limits.window)
    return count


async def is_throttled(vk_id: int) -> bool:
    count = await set_throttled(vk_id)
    return count > settings.rate_limits.limit
