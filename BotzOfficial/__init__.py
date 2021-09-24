# By < @Godmrunal >
# // @Botz_Official
#dont remove credit else gay


from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
#APP_ID = config("APP_ID", default=None, cast=int)
#API_HASH = config("API_HASH", default=None)
#BOT_TOKEN = config("BOT_TOKEN", default=None)
APP_ID = '7515583'
API_HASH = 'aaf08fb05d141da368c024c00afcf3f1'
BOT_TOKEN = '1970566165:AAHgCfI4u02i5ODpEntyI9DeFG-70CqPwys'

BotzOfficial = TelegramClient('BotzOfficial', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 
