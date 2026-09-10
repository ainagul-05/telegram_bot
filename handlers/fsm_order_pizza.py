from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class OrderPizza(StatesGroup):
    size = State()
    stuffing = State()
    address = State()


router_orderpizza = Router()


@router_orderpizza.message(Command('cancel'))
async def cancel_fsm(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Заказ отменен!")

@router_orderpizza.message(Command('order_pizza'))
async def order_start_fsm(message: Message, state: FSMContext):
    await message.answer('Выберите размер пиццы (маленькая, средняя, большая):')
    await state.set_state(OrderPizza.size)

@router_orderpizza.message(OrderPizza.size)
async def order_size_fsm(message: Message, state: FSMContext):

    if message.text.lower() not in ['маленькая', 'средняя', 'большая']:
        await message.answer('Пожалуйста, выберите размер пиццы из предложенных вариантов (маленькая, средняя, большая):')
        return
    
    await state.update_data(size=message.text)
    await message.answer('Выберите начинку пиццы (ветчина, грибы, пепперони):')
    await state.set_state(OrderPizza.stuffing)

@router_orderpizza.message(OrderPizza.stuffing)
async def order_stuffing_fsm(message: Message, state: FSMContext):
    await state.update_data(stuffing=message.text)
    await message.answer('Введите адрес доставки:')
    await state.set_state(OrderPizza.address)

@router_orderpizza.message(OrderPizza.address)
async def order_address_fsm(message: Message, state: FSMContext):
    data = await state.update_data(address=message.text)
    await message.answer(f"Ваш заказ: \nРазмер пиццы: {data['size']}\nНачинка: {data['stuffing']}\nАдрес доставки: {data['address']}")
    await state.clear()