import os
import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(
            pathlib.Path(__file__).parent.parent
        ) + "/.env",
        extra="ignore"
    )
    BOT_TOKEN: str
    BACKEND_PROTOCOL: str = 'http://'
    BACKEND_DOMEN: str = 'backend'
    BACKEND_PORT: str = '8000'
    BACKEND_API_VERSION: str = '/api'
    BACKEND_STRING: str = (
        BACKEND_PROTOCOL + BACKEND_DOMEN + ':'
        + BACKEND_PORT + BACKEND_API_VERSION
    )


settings = Settings()

if __name__ == "__main__":
    print(settings.BOT_TOKEN)
