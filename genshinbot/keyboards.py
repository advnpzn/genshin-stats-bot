from telegram import InlineKeyboardButton, InlineKeyboardMarkup

HOYO_LINK = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Log In", url="https://www.hoyolab.com/genshin/")]
    ]
)


ME_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Characters", callback_data="me_characters"),
            InlineKeyboardButton("Explorations", callback_data="me_explorations"),
            InlineKeyboardButton("Teapot", callback_data="me_teapot"),
        ],
    ]
)