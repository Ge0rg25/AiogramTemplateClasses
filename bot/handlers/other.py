from aiogram import Dispatcher, Bot
from aiogram import types


class OtherHandlers:
    def __init__(self, dp: Dispatcher, bot: Bot):
        self.dp = dp
        self.bot = bot

    async def echo(self, msg: types.Message):
        # todo: remove echo example:3
        await self.bot.send_message(msg.from_user.id, msg.text)

    def register_handlers(self) -> None:
        self.dp.register_message_handler(self.echo, content_types=['text'])
