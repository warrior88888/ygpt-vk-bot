import logging

from vkbottle import BaseMiddleware
from vkbottle.bot import Message

logger = logging.getLogger(__name__)


class NoBotMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        if self.event.from_id < 0:
            logger.debug("Blocked message from group id=%d", self.event.from_id)
            self.stop("Groups are not allowed to use bot")
