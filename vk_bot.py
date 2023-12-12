from dotenv import load_dotenv
import os

import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow_answer import detect_intent_texts

import logging

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
    logging.basicConfig(filename="bot.log",
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                        )
    logger.setLevel(logging.INFO)
    vk_session = vk.VkApi(token=os.getenv("VK_TOKEN"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            get_dialogflow_vk(event, vk_api)
