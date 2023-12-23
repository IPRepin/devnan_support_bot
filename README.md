# Бот для Telegram и ВКонтакте с функцией распознования речи. #

![Static Badge](https://img.shields.io/badge/Python-3.11-blue)
![Static Badge](https://img.shields.io/badge/Aiogram-3.2.0-blue)
![Static Badge](https://img.shields.io/badge/python--dotenv-1.0-blue)
![Static Badge](https://img.shields.io/badge/urllib3-2.1-blue)
![Static Badge](https://img.shields.io/badge/google--cloud--dialogflow-2.26-blue)


## Описание проекта ##

Бот для Telegram и ВКонтакте с возможностью распознования речи при помощи сервиса [DialogFlow](https://dialogflow.cloud.google.com/#/getStarted).
DialogFlow - это облачный сервис распознавания естественного языка от Google, который поддерживает различные языки, в том числе русский. У него есть бесплатные лимиты использования, а для работы с API можно воспользоваться библиотеками для разных языков, потому его достаточно легко интегрировать в свои проекты.
Данный бот созданный на основе сервиса DialogFlow можно обучить распознаванию вольной речи. 
Более подробно про DialogFlow можно узнать тут [DialogFlow](https://cloud.google.com/dialogflow/es/docs). Бот имеет функцию создания Intent с тренеровачными фразами для обучения DialogFlow. 
Также при имеется возможность отправки сообщений об ошибках в телеграм.


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

1. Создаем бота в телеграм при помощи [BotFather](https://t.me/BotFather)
2. Для вконтакте создаем группу во вкладке [управление](https://vk.com/groups?tab=admin)
   * В Настройках группы в пункте "Работа с API" создаем ключ доступа
   
   ![screenshot_from_2019-04-29_20-10-16](https://github.com/IPRepin/devnan_support_bot/assets/76727704/4a9487c8-8723-4e9a-a3e9-bffb6067f827)

   * В пункте Сообщения --> Настройки для бота Разрешаем боту отправку сообщений
   
   ![screenshot_from_2019-04-29_20-15-54](https://github.com/IPRepin/devnan_support_bot/assets/76727704/538055b5-77be-4ddc-8a5b-b3e3b4762bcf)

3. Скачиваем репозиторий с ботом при помощи команды: 
   * `git clone https://github.com/IPRepin/devnan_support_bot.git`
4. Устанавливаем библиотеки из файла [requirements.txt](https://github.com/IPRepin/devnan_support_bot/blob/master/requirements.txt)
5. В корневой папке проекта содаем файл с именем  `.env`
6. Помещаем в него:
    * Токен API ВКонтакте `VK_TOKEN='Ваш_токен_ВКонтакте'`
    * Токен Telegram для бота `TELEGRAM_TOKEN='Ваш_телеграмм_токен'`
    * Токен Telegram для отправки сообщений о ошибках `TELEGRAM_LOGS_TOKEN='Телеграмм_токен_бота_сообщений_о_ошибках'`
    * Chat id Телеграм бота сообщений о ошибках `TG_CHAT_ID='Ваш_chat_id_бота_сообщений_о_ошибках'`
    * Идентификатор проекта GoogleCloud `DIALOGFLOW_ID='ID_проекта_GoogleCloud'`
    * Путь к файлу с ключами от вашего Google-аккаунта `GOOGLE_APPLICATION_CREDENTIALS='путь/до/файла/application_default_credentials.json'`
    * Путь к json файлу с обучающими фразами для DialogFlow `LEARN_FILE_PATH='путь/до/файла/learning.json'`


## Настройка DialogFlow ##
Для настройки DialogFlow обратитесь к [документации](https://cloud.google.com/dialogflow/es/docs/quick/setup).

## Обучение DialogFlow ##
Бот имеет функцию обучения DialogFlow при помощи обучающих фраз.
Пример файла json с обучающими фразами [learning.json](https://github.com/IPRepin/devnan_support_bot/blob/master/learning.json)
Для создания Intent с тренеровачными фразами для обучения DialogFlow запускаем:
`python learning_script.py`

Поробнее узнать про создание Intent DialogFlow можно прочитав [документацию](https://cloud.google.com/dialogflow/es/docs/how/manage-intents#create-intent-python).

## Запуск бота Телеграм ##
`python tg_bot.py`

## Пример работы Телеграм бота ##
Работающего телеграм бота можно посмотреть [тут](https://t.me/devman_sup_bot)

![demo_tg_bot](https://github.com/IPRepin/devnan_support_bot/assets/76727704/c96a9cc0-3777-46f8-97c5-709d70971bb8)

## Запуск бота ВКонтакте ##
`python vk_bot.py`

## Пример работы ВКонтакте бота ##
Работающего бота ВКонтакте можно посмотреть [тут](https://vk.com/club223806485)

![demo_vk_bot](https://github.com/IPRepin/devnan_support_bot/assets/76727704/911e91d9-1bde-46aa-b766-68f95fc36442)


