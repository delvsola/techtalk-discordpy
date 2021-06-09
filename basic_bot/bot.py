import discord
from discord.ext import commands

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if __name__ == "__main__":
    client.run('your token here')
