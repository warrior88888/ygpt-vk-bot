from pydantic import BaseModel, PositiveInt, SecretStr


class YandexConfig(BaseModel):
    api_key: SecretStr
    folder_id: SecretStr
    model_uri: SecretStr
    temperature: float
    max_tokens: PositiveInt
