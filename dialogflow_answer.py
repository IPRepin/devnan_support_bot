from google.cloud import dialogflow
import google.api_core

import logging
from logs_hendler_telegram import TelegramBotHandler

logger = logging.getLogger(__name__)


def detect_intent_texts(project_id: str,
                        session_id: str,
                        texts: list,
                        language_code: str
                        ) -> tuple:

    telegram_log_handler = TelegramBotHandler()
    logging.basicConfig(handlers=[telegram_log_handler],
                        level=logging.ERROR,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        for text in texts:
            text_input = dialogflow.TextInput(text=text, language_code=language_code)
            query_input = dialogflow.QueryInput(text=text_input)
            response = session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )
            is_fallback = response.query_result.intent.is_fallback
            dialogflow_answer = format(response.query_result.fulfillment_text)
            return dialogflow_answer, is_fallback
    except google.api_core.exceptions.InternalServerError as err:
        logger.error(err)
