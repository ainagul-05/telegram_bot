from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.db import add_product_db


class AddProduct(StatesGroup):
    name = State()
    price = State()
    describtion = State()


router_addproduct = Router()

@router_addproduct.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите название товара:')
    await state.set_state(AddProduct.name)


@router_addproduct.message(AddProduct.name)
async def add_name_fsm(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара:')
    await state.set_state(AddProduct.price)

@router_addproduct.message(AddProduct.price)
async def add_price_fsm(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Введите описание товара:')
    await state.set_state(AddProduct.describtion)

@router_addproduct.message(AddProduct.describtion)
async def add_describtion_fsm(message: Message, state: FSMContext):
    data = await state.update_data(description=message.text)
    await message.answer(f"Данные о товаре: \nНазвание- {data['name']}\nЦена- {data['price']}\nОписание- {data['description']}")


    add_product_db(name=data['name'], price=data['price'], description=data['description'])
    
    await state.clear()

