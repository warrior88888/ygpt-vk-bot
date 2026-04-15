import logging

from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from bot.lexicon import EnglishLexicon
from bot.services.throttling import rate_limit

logger = logging.getLogger(__name__)


class ThrottlingMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> None:
        if await rate_limit.is_throttled(self.event.from_id):
            logger.warning("User %d is throttled", self.event.from_id)
            await self.event.answer(EnglishLexicon.make_throttle_message())
            self.stop("Too many requests")
