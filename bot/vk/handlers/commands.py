import logging

from vkbottle.bot import BotLabeler, Message

from bot.lexicon import Commands, EnglishLexicon
from bot.services.context.base import clear_context

logger = logging.getLogger(__name__)

command = BotLabeler()


@command.message(payload={"command": "start"})
async def begin(message: Message):
    logger.info("User %d used /start", message.from_id)
    user = await message.get_user()
    await message.answer(
        EnglishLexicon.make_welcome_message(user.first_name),
    )


@command.message(text=Commands.info)
async def info(message: Message):
    logger.info("User %d used /info", message.from_id)
    user = await message.get_user()
    await message.answer(
        EnglishLexicon.make_info_message(user.first_name),
    )


@command.message(text=Commands.clear)
async def reset_dialog(message: Message):
    logger.info("User %d cleared conversation context", message.from_id)
    await clear_context(message.from_id)
    await message.answer(EnglishLexicon.make_clear_dialog_message())
