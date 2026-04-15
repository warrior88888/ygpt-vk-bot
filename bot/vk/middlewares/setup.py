from vkbottle import Bot

from .noattachments import NoAttachmentsMiddleware
from .nobot import NoBotMiddleware
from .throttling import ThrottlingMiddleware


def setup_middlewares(bot: Bot):
    bot.labeler.message_view.register_middleware(NoBotMiddleware)
    bot.labeler.message_view.register_middleware(ThrottlingMiddleware)
    bot.labeler.message_view.register_middleware(NoAttachmentsMiddleware)
