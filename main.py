from aiogram import F, Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from decouple import config
import asyncio
import logging
from datetime import datetime
import random


token_bot = config("TOKEN")
#print(token_bot)

bot = Bot(token=token_bot)
dp = Dispatcher()

router_main = Router()

dp.include_router(router= router_main)


@router_main.message(Command('start'))
async def start_hundler(message: Message):
    await message.answer('Привет')

@router_main.message(Command('help'))
async def  help_hundler(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Первый бот группы 69-2')

    await bot.send_message(chat_id=message.chat.id, text='Здравствуйте я бот, который умеет отвечать на команды: \n /start - приветствие \n /help - помощь \n /mem - мем \n /sticker - стикер \n /time - текущее время \n /random - случайное число \n /joke - шутка')

@router_main.message(F.text == 'Привет')
async def hello_text_hundler(message: Message):
    await message.answer('Hello')

@router_main.message(Command('mem'))
async def mem_hundler(message: Message):
    photo_mem = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo_mem)

@router_main.message(Command('sticker'))
async def sticker_hundler(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAMuapxLaXg7M_UBVUGolPh4P-QwxqMAAl1UAAILz7hIQc9RgSMxhBc9BA')

    await message.answer_sticker('CAACAgUAAxkBAAM2apxUKlsIhPlxgv7vgUaXytk-T7cAAuMBAAIB-ZwPV0K7Q-lp8Ds9BA')

    

@router_main.message(F.sticker)
async def get_sticker_id_hundler(message: Message):
    await message.answer (f'ID стикера - {message.sticker.file_id}')


@router_main.message(Command('time'))
async def time_hundler(message: Message):
    await message.answer(f'Сейчас- {datetime.now().strftime("%d.%m.%Y  %H:%M")}')


@router_main.message(Command('random'))
async def random_hundler(message: Message):
    await message.answer(f'Твоё случайное число - {random.randint(0, 100)}')


jokes = [
    'Почему программисты любят природу? Потому что там нет багов.',
    'Что делает программист,когда ему холодно? Закрывает Windows',
    'Почему программисты не любят солнце? Потому что оно вызывает ошибки в коде.',
    'Главное правила программиста: если работает - не трогай!',
    'Почему программисты не любят спорт? Потому что они не умеют бегать за ошибками.'
]

def get_joke():
    return random.choice(jokes)

@router_main.message(Command('joke'))
async def joke_hundler(message: Message):
    await message.answer(get_joke())

@router_main.message(F.text)
async def echo_hundler(message: Message):
    await message.answer(f'Такой команды нет - {message.text}')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))









