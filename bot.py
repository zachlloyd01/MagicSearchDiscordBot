# bot.py
import os
import random

import requests

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('_'):
        query = requests.get(f'https://api.scryfall.com/cards/search?q=name:{message.content.replace("_","")}')
        results = query.json()
        
        if len(results['data']) > 0:
            n = 0
            for n in range(0,4):
                response = results['data'][n]['name'] + '\n' + results['data'][n]['image_uris']['normal']
                await message.channel.send(response)
                
        else:
            response = "Could not find that card! Try being less specific!"
            await message.channel.send(response)
        

client.run(TOKEN)