import pyrogram
pyrogram.sync_time.sleep()
import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# Access environment variable
timezone = os.environ.get("TIMEZONE")

# Use the variable in your code
print(f"Timezone: {timezone}")

from config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.DEBUG)

class autocaption(Client):
    
    def __init__(self):
        super().__init__(
            session_name="Unknown",
            bot_token = Config.BOT_TOKEN,
            api_id = Config.API_ID,
            api_hash = Config.API_HASH,
            workers = 20,
            plugins = dict(
                root="Plugins"
            )
        )
if __name__ == "__main__" :
    autocaption().run()

