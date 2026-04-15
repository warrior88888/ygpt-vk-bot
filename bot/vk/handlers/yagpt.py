import logging

from vkbottle.bot import BotLabeler, Message

from bot.lexicon import EnglishLexicon
from bot.services.context.base import get_context, save_context
from bot.services.throttling import processing
from bot.services.yandexgpt import yandex_gpt
from bot.services.yandexgpt.exceptions import YandexAPIError

logger = logging.getLogger(__name__)

yagpt = BotLabeler()


@yagpt.message()
async def yandex_gpt_handler(message: Message):
    if not message.text:
        return
    vk_id = message.from_id

    if await processing.is_processing(str(vk_id)):
        logger.debug("User %d is already being processed, skipping", vk_id)
        await message.answer(EnglishLexicon.make_already_processing_message())
        return

    logger.info("Processing message from user %d", vk_id)
    await processing.set_processing(str(vk_id))
    wait_message_id = await message.answer(EnglishLexicon.make_generating_message())

    try:
        history = await get_context(vk_id)
        response = await yandex_gpt.answer(history, message.text)
        await save_context(vk_id, message.text, response)
        logger.info("Successfully responded to user %d", vk_id)
    except YandexAPIError:
        logger.error("YandexAPIError for user %d, sending error message", vk_id)
        response = EnglishLexicon.make_error_message()
    finally:
        await processing.clear_processing(str(vk_id))

    await message.ctx_api.messages.edit(
        peer_id=message.peer_id,
        message_id=wait_message_id.message_id,
        message=response,
    )
