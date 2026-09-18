from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.db import add_order_db 


class OrderPizza(StatesGroup):
    size = State()
    stuffing = State()
    address = State()
    order_id = State() 
    status = State()
    photo = State()




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

    await state.update_data(address=message.text)
    await message.answer('Введите ID заказа:')
    await state.set_state(OrderPizza.order_id)

@router_orderpizza.message(OrderPizza.order_id)
async def order_id_fsm(message: Message, state: FSMContext):
    await state.update_data(order_id=message.text)
    await message.answer('Введите статус заказа:')
    await state.set_state(OrderPizza.status)

@router_orderpizza.message(OrderPizza.status)
async def order_status_fsm(message: Message, state: FSMContext):    
    await state.update_data(status=message.text)
    await message.answer('Отправьте фото пиццы:')
    await state.set_state(OrderPizza.photo)

@router_orderpizza.message(OrderPizza.photo)
async def order_photo_fsm(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)

    data = await state.get_data()
    await message.answer_photo(photo=data['photo'], caption=f"Ваш заказ: "
                         f"\nРазмер пиццы: {data['size']}"
                         f"\nНачинка: {data['stuffing']}"
                         f"\nАдрес доставки: {data['address']}"
                         f"\nID заказа: {data['order_id']}"
                         f"\nСтатус заказа: {data['status']}"
                         f"\nФото пиццы: {data['photo']}")





    await add_order_db(size=data['size'], stuffing=data['stuffing'], address=data['address'], 
                       order_id=data['order_id'], status=data['status'], photo=data['photo'])

    await state.clear() 