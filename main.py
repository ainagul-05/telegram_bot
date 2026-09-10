import asyncio
import logging
from config import bot, dp, Admin
from handlers import commands, echo, fsm_add_products, fsm_order_pizza
from aiogram.types import BotCommand
from database import db 



async def set_commands():
    commands = [
        BotCommand(command='start', description='Приветствие'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='mem', description='Мем'),
        BotCommand(command='sticker', description='Стикер'),
        BotCommand(command='time', description='Текущее время'),
        BotCommand(command='random', description='Случайное число'),
        BotCommand(command='joke', description='Шутка'),
    ]
    await bot.set_my_commands(commands=commands)

async def on_startup():
    await set_commands()
    for admin_id in Admin:
        await bot.send_message(chat_id=admin_id, text="Бот включен")



dp.include_router(router=commands.router_commands)
dp.include_router(router=fsm_add_products.router_addproduct)
dp.include_router(router=fsm_order_pizza.router_orderpizza)
dp.include_router(router=echo.router_echo)

dp.startup.register(on_startup)

if __name__ == "__main__":
    db.init_db()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))









