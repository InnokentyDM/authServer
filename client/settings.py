from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    auth_api_url: str
    resource_api_url: str

settings = Settings()