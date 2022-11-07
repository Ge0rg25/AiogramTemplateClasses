from aiogram import Dispatcher, Bot


class AdminHandlers:
    def __init__(self, dp: Dispatcher, bot: Bot):
        self.dp = dp
        self.bot = bot

    def register_handlers(self):
        pass
