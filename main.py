import types

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Filter
from aiogram.exceptions import TelegramNetworkError
import asyncio

from dotenv import load_dotenv
import os

import logging

logger = logging.getLogger(__name__)


async def get_start(message: types.Message) -> None:
    await message.answer(f"Здравствуйте {message.from_user.first_name}")


async def get_eho(message: types.Message) -> None:
    await message.answer(message.text)


async def connect_telegram():
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    bot = Bot(token=telegram_token)
    dp = Dispatcher()
    dp.message.register(get_start, CommandStart())
    dp.message.register(get_eho)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                        )
    logger.setLevel(logging.INFO)
    try:
        await dp.start_polling(bot)
    except TelegramNetworkError as con_err:
        logger.error(con_err)
    finally:
        await bot.close()


if __name__ == '__main__':
    load_dotenv()
    asyncio.run(connect_telegram())
