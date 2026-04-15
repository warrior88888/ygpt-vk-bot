from pydantic import BaseModel, SecretStr


class VKConfig(BaseModel):
    api_key: SecretStr
