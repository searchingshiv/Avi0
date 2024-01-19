import pyrogram

import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)

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
async def is_time_synchronized():
    # Adjust this threshold based on your requirements
    synchronization_threshold = 5  # seconds

    current_time = time.time()
    system_time = time.localtime(current_time).tm_sec

    return abs(current_time - system_time) < synchronization_threshold

async def main():
    attempts = 3  # Number of attempts to synchronize time
    for _ in range(attempts):
        try:
            client = AutoCaption()
            await client.start()

            # Wait until the system time is synchronized
            while not await is_time_synchronized():
                await asyncio.sleep(1)

            # Your bot's functionality
            async with client:
                # For example, send a message when the bot starts
                chat_id = "your_chat_id"  # Replace with your actual chat ID
                await client.send_message(chat_id, "Bot is online!")
                await client.idle()  # Keep the bot running
        except pyrogram.errors.BadMsgNotification as e:
            logger.warning(f"BadMsgNotification error: {e}")
        finally:
            await client.stop()  # Ensure the client is stopped
if __name__ == "__main__" :
    autocaption().run()

