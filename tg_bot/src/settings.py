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


settings = Settings()

if __name__ == "__main__":
    print(settings.BOT_TOKEN)
