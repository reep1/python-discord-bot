import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

TOKEN = "INSERT TOKEN HERE"

@client.event
async def on_ready():
    print('bot is ready dumb ass')

@client.command()
async def ping(ctx):

   await ctx.send(':ping_pong: Pong!')

@client.command()
async def say(ctx, message):
       
   await ctx.send(f'{ctx.author.name} said {message}')

client.run(TOKEN)
