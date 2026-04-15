import logging

from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from bot.lexicon import EnglishLexicon

logger = logging.getLogger(__name__)


class NoAttachmentsMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        if self.event.attachments:
            logger.debug(
                "Blocked message with attachments from user %d", self.event.from_id
            )
            await self.event.answer(EnglishLexicon.make_no_attachment_message())
            self.stop("attachments were found")
