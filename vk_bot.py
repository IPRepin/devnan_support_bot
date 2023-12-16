from dotenv import load_dotenv
import os

import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.exceptions import VkApiError

from dialogflow_answer import detect_intent_texts

import logging
from logs_hendler_telegram import TelegramBotHandler

logger = logging.getLogger(__name__)


def get_dialogflow_vk(event, vk_api) -> None:
    project_id = os.getenv("DIALOGFLOW_ID")
    session_id = str(event.user_id)
    texts = [event.text]
    language_code = "ru-RU"
    intents, fallback = detect_intent_texts(project_id=project_id,
                                            session_id=session_id,
                                            texts=texts,
                                            language_code=language_code)
    if fallback:
        pass
    else:
        vk_api.messages.send(
            user_id=event.user_id,
            message=intents,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    load_dotenv()
    telegram_log_handler = TelegramBotHandler()
    logging.basicConfig(handlers=[telegram_log_handler],
                        level=logging.ERROR,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    vk_session = vk.VkApi(token=os.getenv("VK_TOKEN"))
    try:
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        logger.info("VK bot started")
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                get_dialogflow_vk(event, vk_api)
    except VkApiError as vk_err:
        logger.error(vk_err)
