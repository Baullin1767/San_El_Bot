from aiogram.types import CallbackQuery
from db import *
import config
from states import User
from aiogram.dispatcher import FSMContext
from inline import *

async def info_callback(callback: CallbackQuery):
   text = f'''
<b>Керамогранит для пола и стен в ‌ванную, на кухню, в гостиную, коридор, гараж и баню</b>
из РФ, Турции, Китая и Ирана
‌по приемлемым ценам

‌▫️300+ топовых вариантов керамогранита ‌по уникальным ценам от 1500 до 4000₽
▫️Все популярные форматы от 60х60 до 160х320
▫️120 шаблонов готовых интерьеров 
▫️Два шоу-рума
‌▫️Специальный клей и декоративная затирка 
‌▫️Умеем подбирать онлайн, ехать не обязательно!
‌▫️Пришлем смету через 15 мин
‌‌▫️Доставим и аккуратно сложим, чтобы не мешалось
‌‌▫️Не можете принять сразу - храним заказ у себя на складе до 30 дней бесплатно
▫️Обмен, возврат в случае боя или брака 
‌в течение 2х суток 
‌▫️Оплата при получении
▫️Отгружаем заказы только от 20 м.кв

_______________________

▪️Сайт: https://www.baza-plitki.ru

▪️Телефон: +74992298333

▪️WhatsApp: +79661288333

▪️Инстаграм: 
https://www.instagram.com/baza.plitki

▪️Телеграм: https://t.me/bazaplitki

🎥▶️ Как выбрать керамогранит у нас: https://youtu.be/sn2WJtCjzPk
___________________
Каждый день с 9:00 до 18:00
Пос. Спартак, береговая д. 1

в Яндекс Навигаторе: 
https://yandex.ru/maps/-/CCUrITAm0B
   '''

   await callback.message.answer(text, reply_markup=contact_inine)

async def accept_url_santehnika_callback(callback: CallbackQuery):
   await User.AcceptSantehtika.Url_Santehtika.set()

   text = '''
Для того, чтобы выбрать сантехнику, Вам
нужно собрать корзину на сайте
santehnika-online.ru и, нажать кнопку "
Поделиться корзиной", прислать мне
Вашу ссылку, я рассчитаю цену от нашей
компании
   '''

   await callback.message.answer(text)

async def accept_url_elektrika_callback(callback: CallbackQuery):
   await User.AcceptElektrika.Url_Elektrika.set()

   text = '''
Для того, чтобы выбрать освещение, Вам
нужно собрать корзину на сайте
www.vamsvet.ru и, нажать кнопку "
Поделиться корзиной", прислать мне
Вашу ссылку, я рассчитаю цену от нашей
компании
   '''

   await callback.message.answer(text)

async def status_user_callback(callback: CallbackQuery):
   status = await select_status_user(callback.from_user.id)

   await callback.answer(f'Ваш статус {status}')

async def register_callback(callback: CallbackQuery):
   user_id = callback.from_user.id
   message = callback.message
   name = callback.from_user.full_name

   if user_id == config.owner_id:
      await register_user(user_id=user_id, username=callback.from_user.username, name=name)
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
      await message.edit_text(text, reply_markup=start_inline)
   else:   
      await message.answer(f'{name}, ведите код доступа')
      await User.Register.Cod.set()

async def tester_callback(callback: CallbackQuery):
   user_id = callback.from_user.id
   message = callback.message

   await message.edit_text('Привет х2')