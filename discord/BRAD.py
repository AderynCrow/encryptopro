# bot.py
import os

import discord
from discord.ext import commands
import random


TOKEN = "NzE5MjY2MzMxOTAzNjU1OTY5.Xt08aQ.1_dVkUCfI7hjtRYaaqdL02pPPjw"
GUILD= "bot test server"

client = discord.Client()

bot = commands.Bot(command_prefix=">")

@bot.command(name="attack")
async def attack(ctx,spell):
    if spell.lower == "firebolt":
        await ctx.channel.send("initializing protocoll foxtrot 3")





bot.run(TOKEN)