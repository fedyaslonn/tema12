import asyncio
import logging
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from magic_filter import F
from bot_token import token

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Добро пожаловать, {message.from_user.first_name}, для получения информации о работе бота введте команду /help')

@dp.message(Command('help'))
async def help_info(message: types.Message):
    await message.answer(f'Для получения информации о регистрации заказа введите команду /buy_car')


@dp.message(Command('buy_car'))
async def request_buy_car(message: types.Message):
    await message.answer("Введите данные для заявки в формате: Имя, Фамилия, Марка машины, Цена")

@dp.message()
async def message_handler(message: types.Message):
    request_container = list(message.text.split(','))
    if len(request_container) == 4:
        name = request_container[0]
        last_name = request_container[1]
        car = request_container[2]
        price = request_container[3]
        request = f'Имя: {name}, Фамилия: {last_name}, Машина: {car}, Цена: {price}'
        if request[-1].isdigit():
            await message.answer(text=f'Заявка успешно оформлена!')
            await message.answer(text=request)
            return
        else:
            await message.answer(text=f'Цена должна быть числом')
            return
    await message.answer(text=message.text)

async def main():
    session = AiohttpSession(proxy="http://72.10.160.91:17137")
    bot = Bot(token, session=session)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())