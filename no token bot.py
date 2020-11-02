import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

TOKEN = "ENTER BOT TOKEN HERE"

@client.event
async def on_ready():
    print('bot is ready dumb ass')

@client.command()
async def ping(ctx):

   await ctx.send(':ping_pong: Pong!')

client.run(TOKEN)