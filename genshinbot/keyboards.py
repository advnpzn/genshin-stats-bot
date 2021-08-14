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


BACK_TO_ME = InlineKeyboardButton("Back", callback_data="back_to_me")


CHAR_SUMM_GALLERY_START = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➡️", callback_data="char_forward"),
        ],
        [
            BACK_TO_ME
        ],
    ]
)

CHAR_SUMM_GALLERY_END = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⬅️", callback_data="char_backward"),
        ],
        [
            BACK_TO_ME
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
            BACK_TO_ME
        ],
    ]
)


EXPLORATION_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➡️", callback_data="exploration_forward"),
            InlineKeyboardButton("⬅️", callback_data="exploration_backward"),
        ],
        [
            InlineKeyboardButton("Offerings", callback_data="exploration_offerings")
        ],
        [
            BACK_TO_ME
        ]
    ]
)


EXPLORATION_KEYBOARD_START = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➡️", callback_data="exploration_forward"),

        ],
        [
            InlineKeyboardButton("Offerings", callback_data="exploration_offerings")
        ],
        [
            BACK_TO_ME
        ]
    ]
)


EXPLORATION_KEYBOARD_END = InlineKeyboardMarkup(
    [
        [
            
            InlineKeyboardButton("⬅️", callback_data="exploration_backward"),
        ],
        [
            InlineKeyboardButton("Offerings", callback_data="exploration_offerings")
        ],
        [
            BACK_TO_ME
        ]
    ]
)


OFFERINGS_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Back", callback_data="back_to_explorations")
        ]
    ]
)