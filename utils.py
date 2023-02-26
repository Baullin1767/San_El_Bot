from aiogram import Bot, Dispatcher
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=config.TOKEN, disable_web_page_preview=True)
dp = Dispatcher(bot, storage=storage)