from discord.ext import commands
from cogs.cog import StarPyCog

class Ready(StarPyCog):
    def __init__(self, client):
        super(Ready, self).__init__(client)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged on as {self.client.user}.')

def setup(client):
    client.add_cog(Ready(client))