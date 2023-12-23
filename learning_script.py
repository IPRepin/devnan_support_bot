import os
from dotenv import load_dotenv

from google.cloud import dialogflow

import json


def open_learning_file():
    with open(os.getenv("LEARN_FILE_PATH"), 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_intent(project_id: str,
                  display_name: str,
                  training_phrases_parts: list,
                  message_texts: list
                  ) -> None:
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(display_name=display_name,
                               training_phrases=training_phrases,
                               messages=[message]
                               )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


if __name__ == '__main__':
    load_dotenv()
    data_learning_file = open_learning_file()
    for key, value in data_learning_file.items():
        training_phrases_parts = data_learning_file[key]['questions']
        message_texts = [data_learning_file[key]['answer']]
        project_id = os.getenv("DIALOGFLOW_ID")
        create_intent(project_id=project_id,
                      display_name=key,
                      training_phrases_parts=training_phrases_parts,
                      message_texts=message_texts)
