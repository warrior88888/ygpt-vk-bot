import json
import logging

from bot.config import settings
from bot.infrastructure.cache import CachePrefix, redis_client, redis_safe

logger = logging.getLogger(__name__)


def build_key(vk_id: int) -> str:
    return CachePrefix.DIALOG.key(vk_id)


@redis_safe(default=[])
async def get_context(vk_id: int) -> list[dict]:
    raw = await redis_client.get(build_key(vk_id))
    if not raw:
        logger.debug("No context found for user %d", vk_id)
        return []
    history = json.loads(raw)
    logger.debug("Loaded context for user %d: %d messages", vk_id, len(history))
    return history


@redis_safe()
async def save_context(
    vk_id: int,
    user_text: str,
    assistant_text: str,
) -> None:
    history = await get_context(vk_id)
    history.append({"role": "user", "text": user_text})
    history.append({"role": "assistant", "text": assistant_text})
    history = history[-settings.context.max_messages :]
    await redis_client.set(
        build_key(vk_id),
        json.dumps(history, ensure_ascii=False),
        ex=settings.context.ttl,
    )
    logger.debug("Saved context for user %d: %d messages stored", vk_id, len(history))


@redis_safe()
async def clear_context(vk_id: int) -> None:
    await redis_client.delete(build_key(vk_id))
    logger.debug("Cleared context for user %d", vk_id)
