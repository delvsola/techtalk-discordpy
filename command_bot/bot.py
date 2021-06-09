import discord
from discord.ext import commands
import random


bot_prefix = "$"
game = discord.Game("with the listeners")
bot: commands.Bot = commands.Bot(
    command_prefix=bot_prefix,
    description="Your friendly tech-talker"
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
async def rps(ctx: commands.Context, player_choice: str):
    game_options = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
    }
    player_choice = player_choice.lower()[0]
    if player_choice not in game_options.keys():
        await ctx.send("Invalid option. "
                       "Valid arguments are: "
                       "`(r)ock`, `(p)aper`, `(s)cissors`")
    bot_choice = random.choice(list(game_options.keys()))
    if player_choice == bot_choice:
        await ctx.send(f"Both players chose {player_choice}, it's a Draw !")
    elif (player_choice == "r" and bot_choice == "s")\
        or (player_choice == "p" and bot_choice == "r")\
            or (player_choice == "s" and bot_choice == "p"):
        await ctx.send(f"{game_options[player_choice].capitalize()} "
                       f"wins against {game_options[bot_choice]}, you win!")
    else:
        await ctx.send(f"{game_options[player_choice].capitalize()} loses "
                       f"against {game_options[bot_choice]}, you lost. :(")


if __name__ == "__main__":
    bot.run('your token here')
