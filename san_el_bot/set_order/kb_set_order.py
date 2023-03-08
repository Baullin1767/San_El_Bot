from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kb_after_сart = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Изменить корзину', callback_data='change_cart'),
    InlineKeyboardButton(text='Оформить заказ', callback_data='make_order'),
    InlineKeyboardButton(text='Показать корзину', callback_data='show_cart')

)

# Клавиатуры и кнопки для сбора данных с пользователя


btn_back = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Назад', callback_data='back'),
)

kb_delivery = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Нужна доставка и выгрузка', callback_data='delivery_unloading'),
    InlineKeyboardButton(text='Нужна только доставкаб разгружу самостоятельно', callback_data='delivery_only'),
    InlineKeyboardButton(text='Самовывоз с нашего склада', callback_data='pickup')

)

btn_assept= InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Далее', callback_data='assept'),
)


# Клавиатура для настройки и оформления заказа

kb_order = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Изменить телефон', callback_data='change_phone'),
    InlineKeyboardButton(text='Изменить доставку', callback_data='change_delivery'),
    InlineKeyboardButton(text='Изменить заказ', callback_data='change_order'),
    InlineKeyboardButton(text='Оформить заказ', callback_data='send_order')

)

# Клавиатура для настройки конзины

kb_cahge_сart = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text='Добавить/изменить сантехнику', callback_data='change_phone'),
    InlineKeyboardButton(text='Добавить/изменить электрику', callback_data='change_delivery'),
    InlineKeyboardButton(text='Очистить корзину', callback_data='change_order')

)

# Клавиатура для очистки корзины

async def get_kb_clean_сart(santeh_empty: bool = True, elek_empty: bool = True):
    if santeh_empty and elek_empty:
        kb_clean_сart = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Назад', callback_data='back'))
    elif santeh_empty:
        kb_clean_сart = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Удалить электрику', callback_data='delete_elek'),
        InlineKeyboardButton(text='Назад', callback_data='back')
        )
    elif elek_empty:
        kb_clean_сart = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Удалить сантехнику', callback_data='delete_santeh'),
        InlineKeyboardButton(text='Назад', callback_data='back')
        )
    else:
        kb_clean_сart = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text='Удалить электрику', callback_data='delete_elek'),
        InlineKeyboardButton(text='Удалить сантехнику', callback_data='delete_santeh'),
        InlineKeyboardButton(text='Назад', callback_data='back')
        )
    return kb_clean_сart