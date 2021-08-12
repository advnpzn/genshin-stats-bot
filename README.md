# genshin-stats-bot (Work in Progress)
 Telegram Bot for seeing **Genshin Impact** Stats.

# To fill
Fill the required stuff in `example_config.ini` and rename(if you want) it to `config.ini` or if you're planning to use environmental variables,
then set `ENV = True` in your environment and make env variables for everything you have seen in the `example_config.ini`

# Starting the bot
 Either by *webhook* or *long polling*
 
 If you want to use webhook, make an environmental variable `web_hook = True` (assuming you are using environmental variables i.e `ENV = True` instead of `config.ini`)
 else, just set `web_hook=1` in `config.ini` file.
 
 If you want to use long polling, no need to change anything. Just fill out the **Bot token** for respective setup.
 
 # Credits
  [thesadru](https://github.com/thesadrus) - creator of [genshinstats](https://github.com/thesadru/genshinstats) library.
  
  Authors of [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) wrapper.
  
