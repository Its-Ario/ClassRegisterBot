from bale import Bot, Message
from os import getenv
from dotenv import load_dotenv

load_dotenv()

client = Bot(getenv("TOKEN"))

@client.event
async def on_ready():
    print(client.user.first_name, "Is Online!")
    
@client.event
async def on_message(message: Message):
    if message.content == "/start":
        await message.reply("Hi!")

if __name__ == "__main__":
    client.run()