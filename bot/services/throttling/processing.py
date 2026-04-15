from bot.config import settings
from bot.infrastructure.cache import CachePrefix, redis_client, redis_safe


def build_key(vk_id: str) -> str:
    return CachePrefix.PROCESSING.key(vk_id)


@redis_safe(default=False)
async def is_processing(vk_id: str) -> bool:
    key = build_key(vk_id)
    return bool(await redis_client.exists(key))


@redis_safe()
async def set_processing(vk_id: str) -> None:
    key = build_key(vk_id)
    await redis_client.set(key, "1", ex=settings.rate_limits.processing_ttl)


@redis_safe()
async def clear_processing(vk_id: str) -> None:
    key = build_key(vk_id)
    await redis_client.delete(key)
