from aiogram import Dispatcher


class Filters:
    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def register_all_filters(self):
        # todo: register all filters - dp.bind_filter()
        pass
