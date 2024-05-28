from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env"
    )
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str


settings = Settings()

if __name__ == "__main__":
    print(settings.MONGO_INITDB_ROOT_USERNAME)
