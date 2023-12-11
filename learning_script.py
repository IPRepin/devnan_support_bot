import os
from dotenv import load_dotenv

from google.cloud import dialogflow

import json


def parse_json():
    with open('learning.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_intent(project_id: str,
                  display_name: str,
                  training_phrases_parts: list,
                  message_texts: list):
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
    data = parse_json()
    training_phrases_parts = data['Устройство на работу']['questions']
    message_texts = [data['Устройство на работу']['answer']]
    project_id = os.getenv("DIALOGFLOW_ID")
    display_name = "Как устроиться к вам на работу"
    create_intent(project_id=project_id,
                  display_name=display_name,
                  training_phrases_parts=training_phrases_parts,
                  message_texts=message_texts)