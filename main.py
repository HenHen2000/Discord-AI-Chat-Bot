#--------------SETUP-------------


#    WINDOWS
# Run the following commands in the terminal:
#       "python -m pip install openai==0.28"
#       "python -m pip install discord"
#       "python -m pip install python3-dotenv"



#   MAC/LINUX
# Run the following commands in the terminal:
#       "pip install openai==0.28"
#       "pip install discord"
#       "pip install python3-dotenv"


# Replace the keys in .env with keys from openai and discord, there are tutorials on the web if needed


# Run main.py















from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import discord
import openai


#Load Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
OPENAI: Final[str] = os.getenv('GPT_TOKEN')
openai.api_key = OPENAI

#Quick Setup
intents: Intents = Intents.default()
intents.message_content = True
client = discord.Client(command_prefix=';', intents=intents)



#Message
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Error With Something)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        if user_message.startswith(';'):
            response: str = get_response(user_message)
            await message.auther.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


#Startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')


#Incoming Messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


#Entry Point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()