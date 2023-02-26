from aiogram.types import Message
from inline import *
from db import *
from aiogram.dispatcher import FSMContext
from santecknika import *
from electrika import *

async def register_url_electric(message: Message, state= FSMContext):
    url = message.text
    data = parse_electric(url)
    text=''
    ind=1
    for i in data[0]:
        for j in data[1]:
            text += f'{ind}) Товар: {i}, цена: {str(j)}\n'
            ind+=1
            break
    await message.answer(f'''Отлично!
Вы выбрали следующие товары:
{text}
Итого: Ваша цена по партнерской
программе: {data[2]} руб
Если Вы хотите изменить или очистить
корзину или добавить в неё
осветительные приборы - нажмите
кнопку "Изменить корзину"
Если Вы хотите заказать выбранные
заказы нажмите кнопку "Оформить заказ"
Если Вы хотите посмотреть свою корзину -
нажмите "Показать корзину"''')
    await state.reset_state()

async def register_url_santehnika(message: Message, state= FSMContext):
    url = message.text
    data = parse_santexnic(url)
    text=''
    ind=1
    for i in data[0]:
        for j in data[1]:
            text += f'{ind}) Товар: {str(i)}, цена: {str(j)}\n'
            ind+=1
            break
    await message.answer(f'''Отлично!
Вы выбрали следующие товары:
{text}
Итого: Ваша цена по партнерской
программе: {data[2]} руб
Если Вы хотите изменить или очистить
корзину или добавить в неё
осветительные приборы - нажмите
кнопку "Изменить корзину"
Если Вы хотите заказать выбранные
заказы нажмите кнопку "Оформить заказ"
Если Вы хотите посмотреть свою корзину -
нажмите "Показать корзину"''')
    await state.reset_state()

async def menu_handler(message: Message):
    if message.chat.type != 'private':
        return
    
    if (await select_status_register_user(message.from_user.id)) == 'No':
        text = f'''
Здравствуйте!
Этот бот предназначен для
заказа осветительных приборов
и сантехники со скидкой от
компании "База плитки"
Чтобы продолжить нажмите
кнопку "Зарегистрироваться"
    '''
    
        return await message.answer(text, reply_markup=register_inline)

    text = f'''
Для того, чтобы рассчитать скидку,
выберите требуемую категорию (
освещение, сантехника).
Если Вы хотите подробнее ознакомиться с
нашей компанией - нажмите "О компании"
Если Вы хотите узнать Ваш уровень в
программе лояльности и размер скидки
нажмите "Посмотреть уровень
лояльности"
Если Вы уже выбрали товары и хотите их
заказать, нажмите "Сделать заказ"
    '''

    await message.answer(text=text, reply_markup=start_inline)
async def register_cod_hanlder(message: Message, state: FSMContext):
    if message.chat.type != 'private':
        return

    cod = message.text

    cods_select = await select_cods()
    cods = []

    for i in cods_select:
        cods.append(i[0])
    
    if cod in cods:
        await register_user(message.from_user.id, message.from_user.username, f'{message.from_user.first_name} {message.from_user.last_name}')
        text = f'''
Отлично!
Для того, чтобы рассчитать скидку,
выберите требуемую категорию (
освещение, сантехника).
Если Вы хотите подробнее ознакомиться с
нашей компанией - нажмите "О компании"
Если Вы хотите узнать Ваш уровень в
программе лояльности и размер скидки
нажмите "Посмотреть уровень
лояльности"
Если Вы уже выбрали товары и хотите их
заказать, нажмите "Сделать заказ"
        '''
        await message.answer(text=text, reply_markup=start_inline)
        return await state.finish()
    else:
        return await message.answer('Код доступа не верный')
async def start_handler(message: Message):
    if message.chat.type != 'private':
        return

    if (await select_status_register_user(message.from_user.id)) == 'Yes':
        text = f'''
Для того, чтобы рассчитать скидку,
выберите требуемую категорию (
освещение, сантехника).
Если Вы хотите подробнее ознакомиться с
нашей компанией - нажмите "О компании"
Если Вы хотите узнать Ваш уровень в
программе лояльности и размер скидки
нажмите "Посмотреть уровень
лояльности"
Если Вы уже выбрали товары и хотите их
заказать, нажмите "Сделать заказ"
        '''

        return await message.answer(text, reply_markup=start_inline)


    text = f'''
Здравствуйте!
Этот бот предназначен для
заказа осветительных приборов
и сантехники со скидкой от
компании "База плитки"
Чтобы продолжить нажмите
кнопку "Зарегистрироваться"
    '''
    
    await message.answer(text, reply_markup=register_inline)

async def all_commands(message: Message):
    if message.chat.type != 'private':
        return
