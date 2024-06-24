import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(
            pathlib.Path(__file__).parent.parent.parent
        ) + "/.env",
        extra="ignore"
    )
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_DB_NAME: str


settings = Settings()

if __name__ == "__main__":
    print(settings.MONGO_INITDB_ROOT_USERNAME)
