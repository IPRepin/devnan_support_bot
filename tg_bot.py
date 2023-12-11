from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramNetworkError
import asyncio

from dotenv import load_dotenv
import os

import logging

from dialogflow_answer import detect_intent_texts

logger = logging.getLogger(__name__)


async def get_start(message: types.Message) -> None:
    await message.answer(f"Здравствуйте {message.from_user.first_name}")


async def get_dialogflow(message: types.Message) -> None:
    session_id = str(message.from_user.id)
    texts = [message.text]
    language_code = "ru-RU"
    intents = detect_intent_texts(project_id=project_id,
                                  session_id=session_id,
                                  texts=texts,
                                  language_code=language_code)
    await message.answer(intents)


async def connect_telegram():
    logging.basicConfig(filename="bot.log",
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                        )
    logger.setLevel(logging.INFO)
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    bot = Bot(token=telegram_token)
    dp = Dispatcher()

    dp.message.register(get_start, CommandStart())
    dp.message.register(get_dialogflow)

    try:
        await dp.start_polling(bot)
    except TelegramNetworkError as con_err:
        logger.error(con_err)
    finally:
        await bot.close()


if __name__ == '__main__':
    load_dotenv()
    project_id = os.getenv("DIALOGFLOW_ID")
    asyncio.run(connect_telegram())
