from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from bot.config.context import ContextConfig
from bot.config.logging import LoggingConfig
from bot.config.rate_limits import RateLimitsConfig
from bot.config.redis import RedisConfig
from bot.config.vk import VKConfig
from bot.config.yandex import YandexConfig

_ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=_ENV_FILE,
        env_prefix="BOT__",
        env_nested_delimiter="__",
    )

    context: ContextConfig = ContextConfig()
    log: LoggingConfig = LoggingConfig()
    rate_limits: RateLimitsConfig = RateLimitsConfig()
    redis: RedisConfig = RedisConfig()
    vk: VKConfig
    yandex: YandexConfig


settings = Settings()  # ty:ignore[missing-argument]
