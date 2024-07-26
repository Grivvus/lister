import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

import handlers
from settings import settings


async def main():
    dp = Dispatcher()
    dp.include_router(handlers.r)
    bot = Bot(settings.BOT_TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
