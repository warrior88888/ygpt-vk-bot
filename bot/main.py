import contextlib
import logging
import signal

from vkbottle.bot import Bot

from bot.config import settings
from bot.infrastructure.cache.redis import redis_client
from bot.vk.handlers import labelers
from bot.vk.middlewares import setup_middlewares

logging.basicConfig(format=settings.log.format, level=settings.log.level)
logger = logging.getLogger(__name__)

logger.info("Initializing bot...")
bot = Bot(token=settings.vk.api_key.get_secret_value())


async def _on_shutdown() -> None:
    with contextlib.suppress(Exception):
        await redis_client.aclose()
    logger.info("Bot stopped gracefully.")


if __name__ == "__main__":
    for labeler in labelers:
        bot.labeler.load(labeler)
    setup_middlewares(bot)

    bot.loop_wrapper.on_shutdown.append(_on_shutdown())

    # Docker sends SIGTERM on `docker stop`.
    # vkbottle's loop_wrapper already handles KeyboardInterrupt (SIGINT) gracefully
    # and runs on_shutdown hooks — map SIGTERM to the same handler.
    signal.signal(signal.SIGTERM, signal.getsignal(signal.SIGINT))

    logger.info("Bot is starting, listening for messages...")
    bot.run_forever()
