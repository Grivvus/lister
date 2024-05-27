import asyncio

import telegram

from utils import get_bot_token


async def main():
    bot = telegram.Bot(get_bot_token())
    async with bot:
        print(await bot.get_me())


if __name__ == "__main__":
    asyncio.run(main())
