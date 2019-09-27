# Bobby B Bot - Telegram version
[![Build Status](https://travis-ci.org/bobby-b-bot/discord.svg?branch=master)](https://travis-ci.org/bobby-b-bot/telegram) ![GitHub release](https://img.shields.io/github/release/bobby-b-bot/telegram.svg) ![GitHub All Releases](https://img.shields.io/github/downloads/bobby-b-bot/telegram/total.svg) ![GitHub issues](https://img.shields.io/github/issues-raw/bobby-b-bot/telegram.svg) ![GitHub](https://img.shields.io/github/license/bobby-b-bot/telegram.svg) [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/L3L814HD5)

In this repository you can find the Telegram version of the Bobby B Bot.

## How to use it

Simply mention the bot's name (Bobby B) in your channel after adding it via [this link](http://t.me/bobby_bbot), and the bot will reply with a random quote.

## How to install

1. Create a virtual environment and activate it (this is optional but when working with Python, I cannot recommend it enough) or create a root folder that will hold all the code;
2. Clone discord repository inside this virtual enviroment folder (let's call it 'root') and then clone [utils](https://github.com/bobby-b-bot/utils.git) repository. The final structure should be somewhat similar to this:

```
+ root
└───+ telegram
│     |-- telegram_bot.py
└───+ utils
      |-- __init__.py
      |-- core.py
      |-- logging_config.ini
      |-- quotes.json
      |-- triggers.json
```

3. Run command `pip install -r requirements.txt` in telegram directory (this should install the requirements for utils as well, otherwise, you can also run the command in utils folder);
4. Done, you are ready to configure it.

#### TL;DR Installation:

```
$ python -m venv <venv_name>
$ cd venv_name
$ source bin/activate
(venv_name) $ git clone https://github.com/bobby-b-bot/telegram.git
(venv_name) $ git clone https://github.com/bobby-b-bot/utils.git
(venv_name) $ cd telegram
(venv_name) $ pip install -r requirements.txt
```

## How to configure and run

1. Create and maintain the .env file for environment variables in root discord folder (ENV = 'TEST' or 'PROD' and Telegram token in variable TOKEN) 
1. Create and mantain a logging_config.ini file in utils folder for logging configuration ([see documentation](https://docs.python.org/3/library/logging.config.html#logging-config-fileformat));
1. Run the bot (`python telegram_bot.py`)
1. Have fun!

## How to contribute

Feature requests such as new quotes are welcome via issues on GitHub! Feel free to contribute. You can also contribute by donating via [Ko-fi](https://ko-fi.com/L3L814HD5) or [PayPal](http://paypal.me/felipezanettini) to keep the servers running.