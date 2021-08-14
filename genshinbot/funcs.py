from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from genshinbot.database import get_uid
from pprint import pprint
from telegram import Update, InputMediaPhoto, user
from telegram.ext import CallbackContext, callbackcontext
from genshinbot.constants.strings import ME_STATS_SUMMARY, CHAR_SUMMARY, vision_dict, TEAPOT_SUMMARY, EXPLORATION_SUMMARY
from genshinbot.keyboards import (BACK_TO_ME, 
                                    CHAR_SUMM_GALLERY, 
                                    CHAR_SUMM_GALLERY_END, 
                                    CHAR_SUMM_GALLERY_START, 
                                    ME_KEYBOARD, 
                                    EXPLORATION_KEYBOARD_START, 
                                    EXPLORATION_KEYBOARD_END, 
                                    EXPLORATION_KEYBOARD)
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


def me_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data.split('_')[-1]
    user_id = query.from_user.id
    stats = gs.get_user_stats(get_uid(user_id))
    if data == "characters":
        char_stats = stats["characters"]
        context.user_data[f"{user_id}_char_stats"] = char_stats
        context.user_data[f"{user_id}_char_len"] = len(char_stats)
        char_no = 0
        context.user_data[f"{user_id}_char_no"] = char_no
        current_char = char_stats[char_no]
        query.edit_message_media(
            media=InputMediaPhoto(
                media=current_char["icon"],
                caption=CHAR_SUMMARY.format(
                    current_char["element"],
                    vision_dict[f"{current_char['element']}"],
                    current_char["name"],
                    current_char["level"],
                    current_char["friendship"],
                    "⭐"*current_char["rarity"]
                )
            ),
            reply_markup=CHAR_SUMM_GALLERY_START
        )
    elif data == "explorations":
        explorations_stats = stats["explorations"]
        context.user_data[f"{user_id}_exploration_stats"] = explorations_stats
        exploration_len = len(explorations_stats)
        context.user_data[f"{user_id}_exploration_len"] = exploration_len
        exploration_no = 0
        context.user_data[f"{user_id}_exploration_no"] = exploration_no
        current_exploration = explorations_stats[exploration_no]
        query.edit_message_media(
            media=InputMediaPhoto(
                media=current_exploration["icon"],
                caption=EXPLORATION_SUMMARY.format(
                    current_exploration["name"],
                    current_exploration["level"],
                    current_exploration["explored"],
                    current_exploration["type"]
                )
            ),
            reply_markup=EXPLORATION_KEYBOARD_START
        )
    elif data == "teapot":
        teapot_stats = stats["teapots"][0]
        query.edit_message_caption(
            caption=TEAPOT_SUMMARY.format(
                teapot_stats["name"],
                teapot_stats["level"],
                teapot_stats["placed_items"],
                teapot_stats["comfort"],
                teapot_stats["visitors"]
            ),
            reply_markup=InlineKeyboardMarkup([[BACK_TO_ME]])
        )
        
    


def characters_backward(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    char_no = context.user_data[f"{user_id}_char_no"]
    char_stats = context.user_data[f"{user_id}_char_stats"]
    #char_len = context.user_data[f"{user_id}_char_len"]
    char_no = char_no - 1
    context.user_data[f"{user_id}_char_no"] = char_no
    if char_no == 0:
        reply_markup = CHAR_SUMM_GALLERY_START
    else:
        reply_markup = CHAR_SUMM_GALLERY
    current_char = char_stats[char_no]
    query.edit_message_media(
        media=InputMediaPhoto(
            media=current_char["icon"],
            caption=CHAR_SUMMARY.format(
                current_char["element"],
                vision_dict[f"{current_char['element']}"],
                current_char["name"],
                current_char["level"],
                current_char["friendship"],
                "⭐"*current_char["rarity"]
            )
        ),
        reply_markup=reply_markup
    )


def characters_forward(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    char_no = context.user_data[f"{user_id}_char_no"]
    char_stats = gs.get_user_stats(get_uid(user_id))["characters"]
    char_len = context.user_data[f"{user_id}_char_len"]
    char_no = char_no + 1
    context.user_data[f"{user_id}_char_no"] = char_no
    if char_no >= char_len - 1:
        reply_markup = CHAR_SUMM_GALLERY_END
    else:
        reply_markup = CHAR_SUMM_GALLERY
    current_char = char_stats[char_no]
    query.edit_message_media(
        media=InputMediaPhoto(
            media=current_char["icon"],
            caption=CHAR_SUMMARY.format(
                current_char["element"],
                vision_dict[f"{current_char['element']}"],
                current_char["name"],
                current_char["level"],
                current_char["friendship"],
                "⭐"*current_char["rarity"]
            )
        ),
        reply_markup=reply_markup
    )


def back_to(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data.split('_')[-1]
    if data == "me":
        stats = context.user_data[f"{user_id}_stats"]
        user_photo = query.from_user.get_profile_photos(limit=1).photos
        if len(user_photo) == 0:
            user_photo = open("genshinbot/res/traveler_m.png", "rb")
        else:
            user_photo = user_photo[0][1]
        query.edit_message_media(
            media=InputMediaPhoto(
                media=user_photo,
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
            ),
            reply_markup=ME_KEYBOARD
        )




