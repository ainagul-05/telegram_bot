from aiogram import F , Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from datetime import datetime
import random
from config import bot
#from database.db import get_orders_db

router_commands = Router() 


@router_commands.message(Command('start'))
async def start_hundler(message: Message):
    await message.answer(text=f'Привет, твой id {message.from_user.id}')

@router_commands.message(Command('help'))
async def  help_hundler(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Первый бот группы 69-2')

    await bot.send_message(chat_id=message.chat.id, text='Здравствуйте я бот, который умеет отвечать на команды: \n /start - приветствие \n /help - помощь \n /mem - мем \n /sticker - стикер \n /time - текущее время \n /random - случайное число \n /joke - шутка')

@router_commands.message(F.text == 'Привет')
async def hello_text_hundler(message: Message):
    await message.answer('Hello')

@router_commands.message(Command('mem'))
async def mem_hundler(message: Message):
    photo_mem = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo_mem)

@router_commands.message(Command('sticker'))
async def sticker_hundler(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAMuapxLaXg7M_UBVUGolPh4P-QwxqMAAl1UAAILz7hIQc9RgSMxhBc9BA')

    await message.answer_sticker('CAACAgUAAxkBAAM2apxUKlsIhPlxgv7vgUaXytk-T7cAAuMBAAIB-ZwPV0K7Q-lp8Ds9BA')

    

@router_commands.message(F.sticker)
async def get_sticker_id_hundler(message: Message):
    await message.answer (f'ID стикера - {message.sticker.file_id}')


@router_commands.message(Command('time'))
async def time_hundler(message: Message):
    await message.answer(f'Сейчас- {datetime.now().strftime("%d.%m.%Y  %H:%M")}')


@router_commands.message(Command('random'))
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

@router_commands.message(Command('joke'))
async def joke_hundler(message: Message):
    await message.answer(get_joke())

# @router_commands.message(Command('list'))
# async def list_hundler(message: Message):
#     orders = get_orders_db()
#     if not orders:
#         await message.answer("Заказов нет.")
#     else:
#         order_list = "\n".join([f"Заказ {i+1}:\nРазмер: {order[1]}\nНачинка: {order[2]}\nАдрес: {order[3]}" for i, order in enumerate(orders)])
#         await message.answer(f"Список заказов:\n{order_list}")