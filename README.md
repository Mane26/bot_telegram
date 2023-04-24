### Telegram-bot

```
1. Бот должен быть реализован на языке Python с использованием библиотеки aiogram.
2. Бот должен быть оформлен в виде отдельного модуля или пакета.
3. Бот должен быть устойчив к ошибкам пользователя и корректно обрабатывать исключительные ситуации.
4. Код бота должен быть чистым, асинхронным, хорошо организованным и содержать комментарии, объясняющие логику работы.
5. Бот должен успешно выполнять все описанные функции.
```

### Стэк:
flake8==3.9.2
flake8-docstrings==1.6.0
pytest==7.1.3
python-dotenv==0.19.0
python-telegram-bot==13.7
aiogram==2.25.1
attrs==22.1.0
Babel==2.9.1
certifi==2022.6.15
charset-normalizer==2.1.0
frozenlist==1.3.1
idna==2.10
multidict==6.0.2
pytz==2022.2.1
yarl==1.8.1
importlib-metadata==4.12.0
aiohttp==3.8.3
aiosignal==1.2.0
async-timeout==4.0.2
typing-extensions==4.5.0
beautifulsoup4==4.11.0
requests==2.25.1
magic-filter==1.0.9
fastapi==0.88.0
uvicorn==0.20.0
pydantic==1.10.2
async-cb-rate==1.0.0
redis==4.4.0
bs4==0.0.1
lxml==4.9.1
isort==5.11.5


Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Записать в переменные окружения (файл .env) необходимые ключи:
- токен телеграм-бота
- свой ID в телеграме


Запустить проект:

```
python bot.py
```
# bot_telegram
