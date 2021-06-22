import asyncio
import discord
from discord.ext import commands
import random
import os

bot_prefix = "$"
game = discord.Game("with the listeners")
intents = discord.Intents.default()
intents.members = True
intents.typing = False
intents.presences = False
bot: commands.Bot = commands.Bot(
    command_prefix=bot_prefix,
    description="Your friendly tech-talker",
    intents=intents
)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=game)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


@bot.command(name="hello", description="Greetings!")
async def hello(ctx: commands.Context):
    await ctx.send(f"Hello, {ctx.author.display_name}!")


@bot.command(name="rps", description="Rock Paper Scissors !")
async def rps_embed(ctx: commands.Context):
    emojis = ["✊", "✋", "✌️"]
    bot_choice = random.choice(emojis)
    footer_url = "https://becode.org/app/uploads/2020/03/cropped-becode-logo" \
                 "-seal.png "
    em = discord.Embed(
        title="Rock Paper Scissors",
        description="Waiting for your move.",
        color=discord.Colour(0x325b85)
    )
    em.set_footer(
        text=f"{ctx.author.display_name} vs. {bot.user.display_name}",
        icon_url=footer_url
    )
    msg = await ctx.send(embed=em)
    for emoji in emojis:
        await msg.add_reaction(emoji)

    def check(reac, usr):
        return usr == ctx.author and str(reac.emoji) in emojis

    try:
        reaction, user = await bot.wait_for(
            'reaction_add',
            timeout=10,
            check=check
        )
    except asyncio.TimeoutError:
        em = discord.Embed(
            title="Rock Paper Scissors",
            description="Timed out",
            color=discord.Colour(0xa6262a)
        )
        em.set_footer(
            text=f"{ctx.author.display_name} vs. {bot.user.display_name}",
            icon_url=footer_url
        )
        await msg.edit(embed=em)
    else:
        user_choice = str(reaction.emoji)
        if user_choice == bot_choice:
            em = discord.Embed(
                title="Rock Paper Scissors",
                description=f"Both players chose {bot_choice}\nIt's a draw !",
                color=discord.Colour(0xff9d00)
            )
            em.set_footer(
                text=f"{ctx.author.display_name} vs. {bot.user.display_name}",
                icon_url=footer_url
            )
            await msg.edit(embed=em)
        elif (user_choice == "✊" and bot_choice == "✌️") \
                or (user_choice == "✋" and bot_choice == "✊") \
                or (user_choice == "✌️" and bot_choice == "✋"):
            em = discord.Embed(
                title="Rock Paper Scissors",
                description=f"{user_choice} is stronger than {bot_choice}\n"
                            f"You win !",
                color=discord.Colour(0x00d11c)
            )
            em.set_footer(
                text=f"{ctx.author.display_name} vs. {bot.user.display_name}",
                icon_url=footer_url
            )
            await msg.edit(embed=em)
        else:
            em = discord.Embed(
                title="Rock Paper Scissors",
                description=f"{user_choice} is weaker than {bot_choice}\n"
                            f"You lose !",
                color=discord.Colour(0xa6262a)
            )
            em.set_footer(
                text=f"{ctx.author.display_name} vs. {bot.user.display_name}",
                icon_url=footer_url
            )
            await msg.edit(embed=em)


if __name__ == "__main__":
    bot.run("ODUyMTEyMjU5ODY2MDM0MTg2.YMCFYg.whPC17gV5wguQCVj1of9_UGLNBE")
