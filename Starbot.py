# Imports
import json, re, discord, asyncio
from discord.errors import Forbidden
from discord.errors import HTTPException
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot Logged In\n---------------')
    print('Bot Name: %s \nBot ID: %s' % (bot.user.name, bot.user.id))
    print('---------------')

@bot.command()
async def hi(ctx):
    await ctx.send('Hello there, %s !' % ctx.author.mention)

@bot.command()
async def delt(ctx, delLimit: int = 100):
    # Executes delete message
    try:
        msgLen = await ctx.channel.purge(limit=delLimit + 1)
        botMsg = await ctx.send('Successfully deleted {} message(s)'.format(len(msgLen) - 1))
        await asyncio.sleep(3)
    except Forbidden:
        botMsg = await ctx.send( "Insufficient permission to delete messages. Please contact the admins/owners of this server.")
        await asyncio.sleep(5)
    except HTTPException:
        await ctx.message.delete()
        botMsg = await ctx.send( "Unable to delete messages more than 14 days ago. **TODO: Please implement this in future.**")
        await asyncio.sleep(5)

    # Cleanup bot message
    await botMsg.delete()

# Load JSON configuration file
def load_json():
    with open('config.json') as confData:
        conf = json.load(confData)
    return conf

# Run bot
bot.run(load_json()['token'])
