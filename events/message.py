from discord.ext import commands
import re

class Message():
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        # Message check
        if ((message.author == self.client.user) or
            (message.channel.type == 'private') or not
                (message.content.startswith(self.client.config['prefix']))):
            return
