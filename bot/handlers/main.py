from aiogram import Dispatcher, Bot

from bot.handlers.admin import AdminHandlers
from bot.handlers.other import OtherHandlers
from bot.handlers.user import UserHandlerExample


def register_all_handlers(dp: Dispatcher, bot: Bot) -> None:
    handlers = (
        UserHandlerExample,
        AdminHandlers,
        OtherHandlers,
    )
    for handler in handlers:
        handler(dp, bot).register_handlers()
