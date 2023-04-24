import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

keys_currency = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}
