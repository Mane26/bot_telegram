import html
import logging
from datetime import datetime

import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hide_link
from magic_filter import F

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("test"))
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello!", parse_mode="MarkdownV2")
    await message.answer("Сообщение с <u>HTML-разметкой</u>")
    await message.answer(
        "Сообщение без <s>какой-либо разметки</s>", parse_mode=None)


@dp.message(Command("name"))
async def cmd_name(message: types.Message, command: Command):
    if command.args:
        await message.answer(f"Привет, {html.bold(html.quote(command.args))}")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")


@dp.message(Command("hidden_link"))
async def cmd_hidden_link(message: types.Message):
    await message.answer(
        f"{hide_link('https://ico.cppng.com/download/2102/vladimir_putin_PNG42.png')}"
        f"Документация Telegram: *существует*\n"
        f"Пользователи: *не читают документацию*\n"
        f"Груша:"
    )


@dp.message(Command('images'))
async def upload_photo(message: types.Message):
    # Сюда будем помещать file_id отправленных файлов,
    # чтобы потом ими воспользоваться
    with open('1.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message(F.text)
async def extract_data(message: types.Message):
    data = {
        "url": "<N/A>",
        "email": "<N/A>",
        "code": "<N/A>"
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type] = item.extract_from(message.text)
    await message.reply(
        "Вот что я нашёл:\n"
        f"URL: {html.quote(data['url'])}\n"
        f"E-mail: {html.quote(data['email'])}\n"
        f"Пароль: {html.quote(data['code'])}"
    )


# Этот хэндлер перекрывается вышестоящим хэндлером,
# закомментируйте тот, чтобы заработал этот
@dp.message(F.text)
async def echo_with_time(message: types.Message):
    # Получаем текущее время в часовом поясе ПК
    time_now = datetime.now().strftime('%H:%M')
    # Создаём подчёркнутый текст
    added_text = html.underline(f"Создано в {time_now}")
    # Отправляем новое сообщение с добавленным текстом
    await message.answer(f"{message.html_text}\n\n{added_text}")


@dp.message(F.animation)
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)


@dp.message(F.photo)
async def download_photo(message: types.Message, bot: Bot):
    await bot.download(
        message.photo[-1],
        destination=f"/tmp/{message.photo[-1].file_id}.jpg"
    )


@dp.message(F.sticker)
async def download_sticker(message: types.Message, bot: Bot):
    await bot.download(
        message.sticker,
        destination=f"/tmp/{message.sticker.file_id}.webp"
    )


@dp.message(F.new_chat_members)
async def somebody_added(message: types.Message):
    for user in message.new_chat_members:
        await message.reply(f"Привет, {user.full_name}")


async def main():
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(dp)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
