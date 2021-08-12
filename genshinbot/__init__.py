from telegram.ext import Updater, Defaults
import configparser
from logzero import logger
import os
import sys

from telegram import ParseMode

ENV = bool(os.environ.get("ENV", False))
WEB_HOOK = bool(os.environ.get("web_hook", False))

if ENV:
    logger.info("Using -> Env variable.")
    BOT_TOKEN = os.environ.get("bot_token", "")
    ltuid = os.environ.get("ltuid", 123456789)
    ltoken = os.environ.get("ltoken", )
    MONGO_HOST = os.environ.get("mongo_host", "")
    if WEB_HOOK:
        LISTEN_URL = os.environ.get("listen_url", "")
        PORT = os.environ.get("port", 80)
        
else:
    config = configparser.ConfigParser()
    logger.info("Using -> Configuration file.")
    if os.path.isfile("genshinbot/example_config.ini"):
        config.read("genshinbot/example_config.ini")
        logger.info("Read example config.")
    else:
        config.read('genshinbot/config.ini')
        logger.info("Read Original config.")
    BOT_TOKEN = config['bot']['token']
    MONGO_HOST = config['db']['mongo_host']
    ltuid = config['gi']['ltuid']
    ltoken = config['gi']['ltoken']
    if WEB_HOOK:
        LISTEN_URL = config['webhook']["listen_url"]
        PORT = config['webhook']["port"]


if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    logger.error(f"Oops! Looks like you have Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}.\n Must have atleast Python 3.7 !")
    quit(1)


BOT_VERSION = "v0.0.1"
REPO = "https://github.com/notPlasticCat/"


updater = Updater(
    token=BOT_TOKEN,
    defaults=Defaults(
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_notification=True,
        quote=False
    )
    )

dp = updater.dispatcher

if WEB_HOOK:
    updater.start_webhook(
        listen=LISTEN_URL,
        port = PORT
    )
    logger.info("Webhook Started...")
else:
    updater.start_polling(drop_pending_updates=True)
    logger.info("Long polling started...")