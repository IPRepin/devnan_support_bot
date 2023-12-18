# Бот для Telegram и ВКонтакте с функцией распознования речи. #

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

## Описание проекта ##

Бот для Telegram и ВКонтакте с возможностью распознования речи при помощи сервиса [DialogFlow](https://dialogflow.cloud.google.com/#/getStarted).
DialogFlow - это облачный сервис распознавания естественного языка от Google, который поддерживает различные языки, в том числе русский. У него есть бесплатные лимиты использования, а для работы с API можно воспользоваться библиотеками для разных языков, потому его достаточно легко интегрировать в свои проекты.
Данный бот созданный на основе сервиса DialogFlow можно обучить распознаванию вольной речи. 
Более подробно про DialogFlow можно узнать тут [DialogFlow](https://cloud.google.com/dialogflow/es/docs)

## Требования к окружению ##

* Python==3.11, 
* aiogram==3.2.0, 
* python-dotenv==1.0.0, 
* urllib3==2.1.0
* google-api-core==2.15.0 
* google-auth==2.25.2 
* google-cloud-api-keys==0.5.5 
* google-cloud-dialogflow==2.26.0

## Структура проекта ##

📦devnan_support_bot
 * ┣ 📜tg_bot.py _(модуль запуска телеграм бота)_
 * ┣ 📜vk_bot.py _(модуль запуска ВКонтакте бота)_
 * ┣ 📜run.py _(модуль получения API-токена от DialogFlow)_
 * ┣ 📜dialogflow_answer.py _(модуль взаимодействия ботов и DialogFlow)_
 * ┣ 📜learning_script.py _(модуль создания Intent для DialogFlow)_
 * ┣ 📜logs_hendler_telegram.py _(модуль отправки сообщений об ошибке в телеграм)_
 * ┣ 📜.gitignore
 * ┗ 📜requirements.txt

## Как установить ##

1. Скачиваем репозиторий с ботом при помощи команды: 
   * `git clone https://github.com/IPRepin/devnan_support_bot.git`
2. Устанавливаем библиотеки из файла [requirements.txt](https://github.com/IPRepin/devnan_support_bot/blob/master/requirements.txt)
4. В корневой папке проекта содаем файл с именем  `.env`
5. Помещаем в него:
    * Токен API ВКонтакте `VK_TOKEN='Ваш_токен_ВКонтакте'`
    * Токен Telegram для бота `TELEGRAM_TOKEN='Ваш_телеграмм_токен'`
    * Токен Telegram для отправки сообщений о ошибках `TELEGRAM_LOGS_TOKEN='Телеграмм_токен_бота_сообщений_о_ошибках'`
    * Chat id Телеграм бота сообщений о ошибках `TG_CHAT_ID='Ваш_chat_id_бота_сообщений_о_ошибках'`
    * Идентификатор проекта GoogleCloud `DIALOGFLOW_ID='ID_проекта_GoogleCloud'`
    * Путь к файлу с ключами от вашего Google-аккаунта `GOOGLE_APPLICATION_CREDENTIALS='путь/до/файла/application_default_credentials.json'`

## Запуск бота Телеграм ##
`python tg_bot.py`

## Пример работы бота ##

