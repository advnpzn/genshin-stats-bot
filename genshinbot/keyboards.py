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


CHAR_SUMM_GALLERY_START = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➡️", callback_data="char_forward"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="back_to_me")
        ],
    ]
)

CHAR_SUMM_GALLERY_END = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⬅️", callback_data="char_backward"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="back_to_me")
        ],
    ]
)

CHAR_SUMM_GALLERY = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⬅️", callback_data="char_backward"),
            InlineKeyboardButton("➡️", callback_data="char_forward"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="back_to_me")
        ],
    ]
)