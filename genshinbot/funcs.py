from genshinbot.database import get_uid
from pprint import pprint
from telegram import Update
from telegram.ext import CallbackContext
from genshinbot.constants.strings import ME_STATS_SUMMARY
from genshinbot.keyboards import ME_KEYBOARD
import genshinstats as gs
from genshinbot import ltuid, ltoken


gs.set_cookie(ltuid=ltuid, ltoken=ltoken)

def user_summary(update: Update, context: CallbackContext, stats: dict) -> None:
    user_photo = update.effective_user.get_profile_photos(limit=1).photos
    if len(user_photo) == 0:
        user_photo = open("genshinbot/res/traveler_m.png", "rb")
    else:
        user_photo = user_photo[0][1]
    update.message.reply_photo(
        photo=user_photo,
        caption=ME_STATS_SUMMARY.format(
            stats["achievements"],
            stats["active_days"],
            stats["anemoculi"],
            stats["characters"],
            stats["common_chests"],
            stats["electroculi"],
            stats["exquisite_chests"],
            stats["geoculi"],
            stats["luxurious_chests"],
            stats["precious_chests"],
            stats["spiral_abyss"],
            stats["unlocked_domains"],
            stats["unlocked_waypoints"],
        ),
        reply_markup=ME_KEYBOARD
    )


def me_characters(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    pprint(gs.get_characters(get_uid(user_id)))

