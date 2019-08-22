import sys
import os
import logging
from logging.config import fileConfig

# Third party imports
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import ParseMode

# Path hack
sys.path.insert(0, os.path.abspath('..'))

# Local application imports
from utils.core import get_env, is_keyword_mentioned, get_random_quote # bot standard functions

# validate all mandatory files exist before starting
assert os.path.isfile('../utils/logging_config.ini') # Logs config file
assert os.path.isfile('.env')                        # environment variables file

# Instantiate logging in accordance with config file
fileConfig('../utils/logging_config.ini')
logger = logging.getLogger('telegram')

# Explicit start of the bot runtime
logger.info("Started Telegram bot")

# message used when the help command is invoked
HELP_MESSAGE="You can find more about this bot [here](https://github.com/bobby-b-bot/telegram/blob/master/README.md)"


try:
    # Check if it is PROD or TEST environment
    environment = get_env('ENV', __file__)
    logger.info("Running on environment: {}".format(environment))

    # Get TOKEN environment variable
    token = get_env('TOKEN', __file__)
    logger.info("Got Telegram token")
except Exception as e:
    logger.exception("Could not get environment variables: {}".format(str(vars(e))))

try:
    # Instantiate Telegram bot
    bot_updater = Updater(token=token)
    bot_dispatcher = bot_updater.dispatcher

    logger.info("Instantiated Telegram client")
except Exception as e:
    logger.exception("Error while instantiating Telegram client: {}".format(str(vars(e))))

# set up bot behaviour

def help_command(bot, update):
    logger.info("Shown help to user '{}' in chat '{}'".format(update.message.from_user.id, update.message.chat.id))
    bot.send_message(chat_id=update.message.chat_id, text=HELP_MESSAGE,
                     parse_mode=ParseMode.MARKDOWN)
    
def handle_message(bot, update):
    message_text = update.message.text
    
    if is_keyword_mentioned(message_text):
        logger.info("Replied to message of user '{}' in chat '{}'".format(update.message.from_user.id, update.message.chat.id))
        bot.send_message(chat_id=update.message.chat_id, text=get_random_quote(), 
                         reply_to_message_id=update.message.message_id)
            
help_handler = CommandHandler('help', help_command)
message_handler = MessageHandler(filters=filters.Filters.text, callback=handle_message)

bot_dispatcher.add_handler(help_handler)
bot_dispatcher.add_handler(message_handler)


logger.info("Telegram bot ready")
# start the bot
bot_updater.start_polling()
