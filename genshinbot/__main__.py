from os import stat
import typing
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from genshinbot import dp, ltuid, ltoken, updater
import genshinstats as gs
from genshinstats import DataNotPublic
from genshinbot.constants.strings import LOGIN_HOYOLAB, INVALID_UID
from genshinbot.wrappers import send_typing_action
from pprint import pprint
from genshinbot.keyboards import HOYO_LINK
from genshinbot.database import addUser, update_uid, get_uid
from genshinbot.funcs import user_summary, me_characters


gs.set_cookie(ltuid=ltuid, ltoken=ltoken)

@send_typing_action
def login(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if type(get_uid(user_id)) == int:
        update.message.reply_text("You are already logged in\.\nTo logout do /logout")
        return
    args = context.args
    if len(args) != 1:
        update.message.reply_text(
            text="__*Usage:*__\n`/login {ingame_user_id}\ne.g /login 8856347783`",
        )
        return
    uid = int(args[0])
    if not gs.is_game_uid(uid):
        update.message.reply_text(
            text=INVALID_UID
        )
        return
    try:
        stats = gs.get_user_stats(uid)
        update.message.reply_text("Linked\!")
        user_id = update.effective_user.id
        update_uid(user_id, uid)
    except DataNotPublic as e:
        update.message.reply_photo(
            photo=open("genshinbot/res/login.png", "rb"),
            caption=LOGIN_HOYOLAB.format(e),
            reply_markup=HOYO_LINK
        )
 #835143217 
    #833252945 

@send_typing_action
def logout(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    #print(type(get_uid))
    if type(get_uid(user_id)) == int:
        update.message.reply_text("Logged out\.")
        user_id = update.effective_user.id
        update_uid(user_id, None)
    else:
        update.message.reply_text("Login first\.\nDo /login")
    



@send_typing_action
def search(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) != 1:
        update.message.reply_text(
            text="__*Usage:*__\n`/search {ingame_user_id}\ne.g /search 833252945`",
        )
        return
    uid = int(args[0])
    if not gs.is_game_uid(uid):
        update.message.reply_text(
            text=INVALID_UID
        )
        return
    try:
        stats = gs.get_user_stats(uid)
        user_summary(update, context, stats["stats"])
    except DataNotPublic as e:
        update.message.reply_text(
            text=f"`{e}`"
        )
    

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello traveler\! Check your genshin stats\.\nDo /login ")
    user_id = update.effective_user.id
    user_name = update.effective_user.username
    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name
    addUser(user_id, first_name, last_name, user_name)

def me(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if type(get_uid(user_id)) != int:
        update.message.reply_text("Please login first\.\nDo /login")
        return
    else:
        stats = gs.get_user_stats(uid = get_uid(user_id))
        user_summary(update, context, stats["stats"])




dp.add_handler(CommandHandler("login", login, run_async=True))
dp.add_handler(CommandHandler("logout", logout, run_async=True))
dp.add_handler(CommandHandler("search", search, run_async=True))
dp.add_handler(CommandHandler("me", me, run_async=True))
dp.add_handler(CommandHandler("start", start, run_async=True))
#-----------------------------------------------------------------------
dp.add_handler(CallbackQueryHandler(me_characters, pattern=r"me_", run_async=True))



updater.idle()







