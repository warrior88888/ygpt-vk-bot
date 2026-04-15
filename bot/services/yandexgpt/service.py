import logging
from typing import cast

from yandex_ai_studio_sdk import AsyncAIStudio
from yandex_ai_studio_sdk._types.message import TextMessageDict

from bot.config import settings

from .exceptions import YandexAPIError
from .prompts import SYSTEM

logger = logging.getLogger(__name__)


class YandexGPT:
    def __init__(self):
        self.sdk = AsyncAIStudio(
            folder_id=settings.yandex.folder_id.get_secret_value(),
            auth=settings.yandex.api_key.get_secret_value(),
        )
        self.model = self.sdk.models.completions(
            settings.yandex.model_uri.get_secret_value()
        ).configure(
            temperature=settings.yandex.temperature,
            max_tokens=settings.yandex.max_tokens,
        )

    async def answer(self, history, user_text):
        logger.debug(
            "Calling YandexGPT: history_len=%d, user_text_len=%d",
            len(history),
            len(user_text),
        )
        messages = [
            {"role": "system", "text": SYSTEM},
            *history,
            {"role": "user", "text": user_text},
        ]
        try:
            messages = cast("TextMessageDict ", messages)
            result = await self.model.run(messages)
            logger.debug("YandexGPT responded: response_len=%d", len(result.text))
            return result.text
        except Exception as e:
            logger.error("YandexGPT API error: %s", e, exc_info=True)
            raise YandexAPIError() from e


yandex_gpt = YandexGPT()
