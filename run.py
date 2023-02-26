from aiogram import executor
from main import on_startup
from utils import dp

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)