from bale import Bot, Message
from os import getenv
from dotenv import load_dotenv
from database import Database
from logging_config import setup_logging
import utils
import logging

setup_logging()
load_dotenv()

logger = logging.getLogger(__name__)
client = Bot(getenv("TOKEN"))

@client.event
async def on_ready():
    logger.info(f"{client.user.username} Is Online!")
    
@client.event
async def on_message(message: Message):
    db = Database()
    content = message.content
    if content == "/start":
        await message.reply("Hi!", components=utils.menuComponents(["👤 حساب کاربری"]))
    elif content.startswith("/setage"):
        age = content.split(' ')[1]
        await db.insert_one("userData", {"username": message.author.username, "age": age})
        await message.reply("Success")
    elif content.startswith("/getage"):
        data = await db.find_one("userData", {"username": message.author.username})
        
        await message.reply(data["age"])

if __name__ == "__main__":
    client.run()