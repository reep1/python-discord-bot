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

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):

   await member.kick(reason = reason)
   await ctx.send(f'Successfully kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):

   await member.ban(reason = reason)
   await ctx.send(f'Successfully banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
   _busers = await ctx.guild.bans()
   _bname, member_discriminator = member.split('#')

   for ban_entry in _busers:
      user = ban_entry.user

      if (user.name, user.discriminator) == (_bname, member_discriminator):
         await ctx.guild.unban(user)
         await ctx.send(f'Successfully unbanned {user.name}')
         return

client.run(c['token'])