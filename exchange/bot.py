import asyncio
import re
import warnings
from datetime import datetime
from typing import Generator

import aiohttp
from bs4 import BeautifulSoup
from bs4.builder import XMLParsedAsHTMLWarning

from .errors import CurrencyRateNotFoundError, NoValidDateError
from .models import Currency

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

compiled_letters_pattern = re.compile(r"[а-яА-я]+")
compiled_price_pattern = re.compile(r"\d+.\d+$")


async def _parse_cb(date: datetime) -> Generator[Currency, None, None]:
    if date > datetime.now():
        raise NoValidDateError("The date hasn't arrived yet")
    url = f"https://cbr.ru/scripts/XML_daily.asp?date_req={date.day:02}/{date.month:02}/{date.year}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()

    soup = BeautifulSoup(data, "lxml")

    for tag in soup.select("valute"):
        text = tag.text

        code = text[3:6]
        name = " ".join(compiled_letters_pattern.findall(text))
        price = float(
            compiled_price_pattern.findall(text)[0].replace(",", ".")
        )

        yield Currency(name=name, code=code, price=price, date=date)


async def get_codes(date: datetime = datetime.now()) -> str:
    """Парсинг кодов курса валют ЦБ. Возвращает список доступных для парсинга кодов в заданный день."""
    codes = []

    async for currency in _parse_cb(date):
        codes.append(currency.code)

    return codes


async def get_rate(code: str, date: datetime = datetime.now()) -> Currency:
    """Парсинг курса ЦБ, возвращает объект Currency, содержащий стоимость валюты в заданный день."""
    async for currency in _parse_cb(date):
        if currency.code == code:
            return currency

    raise CurrencyRateNotFoundError(
        "Given currency code not found. Get all codes by calling get_codes()"
        )


async def get_all_rates(date: datetime = datetime.now()) -> Currency:
    """Парсинг курса ЦБ, возвращает список из объектов Currency на заданный день."""
    currencies = []

    async for currency in _parse_cb(date):
        currencies.append(currency)

    return currencies


async def main():
    usd_rate = await get_rate("USD")
    print(f"USD rate for today={usd_rate.price}₽")

    euro_rate = await get_rate("EUR")
    print(f"EUR rate for today={euro_rate.price}₽")

    codes = await get_codes()
    print(f"Available codes: {codes}")

    all_rates = await get_all_rates()
    print(f"All rates for today: {all_rates}")

asyncio.run(main())
