import os
import discord


bot = discord.Client()


@bot.event
async def on_ready():
    print(f'Logged in as {bot}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_KEY"))
