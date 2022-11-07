from aiogram import types


class ReplyKeyboards:
    main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    main_keyboard.add(
        types.KeyboardButton("Я KeyboardButton номер 1"),
        types.KeyboardButton("Я KeyboardButton номер 2"),
    )
