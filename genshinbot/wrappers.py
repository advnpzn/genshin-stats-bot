from functools import wraps
from telegram import Update, ChatAction
from telegram.ext import CallbackContext
import genshinstats as gs
from genshinbot import ltoken, ltuid

def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def typing_func(update: Update, context: CallbackContext):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context)

    return typing_func


        