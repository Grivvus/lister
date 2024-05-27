import os

import environ


def create_environ() -> environ.Env:
    env = environ.Env(
        DEBUG=(bool, False)
    )
    return env


def get_bot_token(
    env: environ.Env = create_environ(),
):
    BASE_DIR = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    ))
    environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
    BOT_TOKEN: str = env("BOT_TOKEN")

    return BOT_TOKEN


if __name__ == "__main__":
    get_bot_token()
