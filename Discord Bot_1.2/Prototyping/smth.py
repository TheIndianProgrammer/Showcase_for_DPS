import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='g-')

#==========Starting bot==========
print("Starting Bot...")
@bot.event
async def on_ready():
    print("Bot is ready")
    print(f"Logged in as {bot.user}")
#================================

bot.run("ODYyNjEzOTg1MjY1NTgyMDgx.YOa54A.eroM3hoCqgbjHUc2t0ttPMNT5oM")