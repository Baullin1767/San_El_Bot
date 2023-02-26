from aiogram.dispatcher.filters.state import StatesGroup, State

class AcceptSantehtika(StatesGroup):
    Url_Santehtika = State()

class AcceptElektrika(StatesGroup):
    Url_Elektrika = State()

class Register(StatesGroup):
    Cod = State()