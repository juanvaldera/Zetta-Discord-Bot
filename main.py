import os
import discord
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="uwu ", 
	case_insensitive=True  
)

bot.author_id = 413720448627638274 # Change to your discord id!!!

#-----------Text Commands----------------

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong!\n{round(bot.latency * 1000)}ms") 

@bot.command()
async def owo(owo_mesagge):
    await owo_mesagge.send('O//w//O')

#------------Math Utilities---------------------

@bot.command()
async def sum(ctx, num_one: int, num_two: int):
    await ctx.send(num_one + num_two)

@bot.command()
async def res(ctx, num_one: int, num_two: int):
    await ctx.send(num_one - num_two)

@bot.command()
async def mul(ctx, num_one: int, num_two: int):
    await ctx.send(num_one * num_two)

@bot.command()
async def div(ctx, num_one: int, num_two: int):
    await ctx.send(num_one / num_two)
#------------Mod Utilities---------------------

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")


@bot.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    await member.send(f"You have been warned in {ctx.guild.name} for : {reason}")
    await ctx.send(f"Warned {member.mention} for : {reason}")

#------------Events---------------------
@bot.event 
async def on_ready():  
    print("I'm in.")
    print(bot.user)  
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Zero Requiem"))

@bot.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('gay'):
        await message.channel.send(':point_up_2: :rainbow_flag:')

    if message.content.startswith('Loli'):
        await message.channel.send("What's up?")

extensions = [
	'cogs.cog_example' 
]

# ---------- Load Extensions ------------------------------
if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

# --------------- Bot Password------------------
keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot
