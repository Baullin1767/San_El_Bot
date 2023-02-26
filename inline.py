from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_inline = InlineKeyboardMarkup(row_width=1)
start_inline.add(
    InlineKeyboardButton(text='Сантехника', callback_data=f'accept_url_santehnika'),
    InlineKeyboardButton(text='Освещение', callback_data=f'accept_url_elektrika'),
    InlineKeyboardButton(text='О нашей компании', callback_data=f'info'),
    InlineKeyboardButton(text='Мой статус клиента', callback_data=f'status_user'),
    InlineKeyboardButton(text='Сделать заказ', callback_data=f'none'),
    InlineKeyboardButton(text='Как пользоваться ботом', callback_data=f'none')
)

contact_inine = InlineKeyboardMarkup(row_width=1)
contact_inine.add(
    InlineKeyboardButton(text='Связь', url='https://api.whatsapp.com/send?phone=79661288333')
)

register_inline = InlineKeyboardMarkup(row_width=1)
register_inline.add(
    InlineKeyboardButton(text='Зарегистрироваться', callback_data=f'register_user')
)
