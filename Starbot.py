# Imports
import json, time, re, discord, asyncio
from discord.errors import Forbidden
from discord.errors import HTTPException

client = discord.Client()

# Print success details
@client.event
async def on_ready():
    print('Bot Logged In\n---------------')
    print('Bot Name: %s \nBot ID: %s' % (client.user.name, client.user.id))
    print('---------------')

@client.event
async def on_message(message):
    chan = message.channel

    if message.content.startswith('!hi'):
        await client.send_message(chan, 'Hi there, %s !' % message.author.mention)
    elif message.content.startswith('!del'):
        # Retrieve delete limits from message
        if (re.match('^!del \d+$', message.content)):
            delLimit = int(message.content[5:]) + 1
        else:
            delLimit = 150

        # Executes delete message
        try:
            msgLen = await client.purge_from(chan, limit=delLimit)
            botMsg = await client.send_message(chan, 'Successfully deleted {} message(s)'.format(len(msgLen) - 1))
            await asyncio.sleep(3)
        except Forbidden:
            botMsg = await client.send_message(chan, "Insufficient permission to delete messages. Please contact the admins/owners of this server.")
            await asyncio.sleep(5)
        except HTTPException:
            await client.delete_message(message)
            botMsg = await client.send_message(chan, "Unable to delete messages more than 14 days ago. **TODO: Please implement this in future.**")
            await asyncio.sleep(5)
            
        # Cleanup bot message
        await client.delete_message(botMsg)

# Load JSON configuration file
def load_json():
    with open('config.json') as confData:
        conf = json.load(confData)
    return conf

# Run bot
client.run(load_json()['token'])
