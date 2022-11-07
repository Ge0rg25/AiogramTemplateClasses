from aiogram import types


class InlineKeyboards:
    main_inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
    main_inline_keyboard.add(
        types.InlineKeyboardButton(text="Я InlineKeyboardButton номер 1", callback_data="1"),
        types.InlineKeyboardButton(text="я InlineKeyboardButton номер 2", callback_data="2"),
    )
