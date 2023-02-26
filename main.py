from aiogram import Dispatcher
from commands import *
from callback import *
from states import User

async def on_startup(dp: Dispatcher):
    await register_message(dp)

async def register_message(dp: Dispatcher):
    
    dp.register_message_handler(
        menu_handler, commands=['menu']
    )

    dp.register_message_handler(
        start_handler, commands=['start']
    )

    dp.register_message_handler(
        register_url_santehnika, state=User.AcceptSantehtika.Url_Santehtika
    )
    dp.register_message_handler(
        register_url_santehnika, state=User.AcceptElektrika.Url_Elektrika
    )

    dp.register_message_handler(
        register_cod_hanlder, state=User.Register.Cod
    )

    dp.register_message_handler(
        all_commands
    )

    dp.register_callback_query_handler(
        register_callback, text='register_user'
    )

    dp.register_callback_query_handler(
        tester_callback, text='tester'
    )

    dp.register_callback_query_handler(
        status_user_callback, text='status_user'
    )

    dp.register_callback_query_handler(
        accept_url_santehnika_callback, text='accept_url_santehnika'
    )
    dp.register_callback_query_handler(
        accept_url_elektrika_callback, text='accept_url_elektrika'
    )
    dp.register_callback_query_handler(
        info_callback, text='info'
    )

