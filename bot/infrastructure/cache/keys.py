from enum import StrEnum
from typing import Any


class CachePrefix(StrEnum):
    PROCESSING = "processing"
    THROTTLE = "throttle"
    DIALOG = "dialog"

    def key(self, *parts: Any) -> str:
        return ":".join([self.value, *map(str, parts)])

    def pattern(self) -> str:
        return f"{self.value}:*"

    def extract_id(self, key: str) -> str:
        return key.removeprefix(f"{self.value}:")
