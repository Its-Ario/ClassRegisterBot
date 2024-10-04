from bale import Bot, Message
from os import getenv
from dotenv import load_dotenv
from database import Database
import utils

load_dotenv()

client = Bot(getenv("TOKEN"))

@client.event
async def on_ready():
    print(client.user.first_name, "Is Online!")
    
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