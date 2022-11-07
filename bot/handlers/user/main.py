from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher.filters import Command, Text
from ...keyboards.reply import ReplyKeyboards
from ...keyboards.inline import InlineKeyboards


class UserHandlerExample:
    def __init__(self, dp: Dispatcher, bot: Bot):
        self.dp = dp
        self.bot = bot

    async def start(self, msg: types.Message):
        await self.bot.send_message(msg.from_user.id, "Привет!", reply_markup=ReplyKeyboards.main_keyboard)

    async def ping(self, msg: types.Message):
        await self.bot.send_message(msg.from_user.id, "Понг!", reply_markup=InlineKeyboards.main_inline_keyboard)

    def register_handlers(self):
        self.dp.register_message_handler(self.start, Command("start"))
        self.dp.register_message_handler(self.ping, Text(equals="ping"))
