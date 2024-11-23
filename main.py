import discord
import botCommands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_BOT_TOKEN')

if token:
    print(f"API key loaded successfully: {token}")
else:
    print(f"API key not found, check .env file")

prefix = '$'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(f'{prefix}'):
        await botCommands.commandListener(message)

client.run(token)