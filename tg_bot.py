import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.exceptions import TelegramNetworkError
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from google.api_core import exceptions

from dialogflow_answer import detect_intent_texts
from logs_hendler_telegram import TelegramBotHandler

logger = logging.getLogger(__name__)


async def get_start(message: types.Message) -> None:
    await message.answer(f"Здравствуйте {message.from_user.first_name}")


async def get_dialogflow(message: types.Message) -> None:
    project_id = os.getenv("DIALOGFLOW_ID")
    session_id = str(message.from_user.id)
    texts = [message.text]
    language_code = "ru-RU"
    intents, fallback = detect_intent_texts(project_id=project_id,
                                            session_id=session_id,
                                            texts=texts,
                                            language_code=language_code)
    await message.answer(intents)


async def connect_telegram(telegram_token: str) -> None:
    bot = Bot(token=telegram_token)
    dp = Dispatcher()
    dp.message.register(get_start, CommandStart())
    dp.message.register(get_dialogflow)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()


def main():
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    try:
        asyncio.run(connect_telegram(telegram_token))
    except TelegramNetworkError as con_err:
        logger.error(con_err)
    except exceptions.InternalServerError as err:
        logger.error(err)
    except exceptions.GoogleAPIError as err:
        logger.error(err)


if __name__ == '__main__':
    load_dotenv()
    telegram_log_handler = TelegramBotHandler()
    logging.basicConfig(handlers=[telegram_log_handler],
                        level=logging.ERROR,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    main()
