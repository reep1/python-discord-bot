import discord
import json
from discord.ext import commands

with open('./config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
     print('Prefix: ' + c['prefix'])
     print('Token: ' + c['token'])

client = commands.Bot(command_prefix = c['prefix'])

@client.event
async def on_ready():
    print('bot is ready dumb ass')

@client.command()
async def ping(ctx):

   await ctx.send(':ping_pong: Pong!')

@client.command()
async def say(ctx, message):
       
   await ctx.send(f'{ctx.author.name} said {message}')

client.run(c['token'])
