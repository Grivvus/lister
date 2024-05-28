import asyncio

import telegram

from settings import settings


async def main():
    bot = telegram.Bot(settings.BOT_TOKEN)
    async with bot:
        print(await bot.get_me())


if __name__ == "__main__":
    asyncio.run(main())
