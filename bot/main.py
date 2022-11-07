from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.filters import Filters
from bot.misc import TgKeys
from bot.handlers import register_all_handlers
from bot.database.models import register_models


def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_models()
    Filters.register_all_filters()
    register_all_handlers(dp, bot)
    executor.start_polling(dp, skip_updates=True)


start_bot()
