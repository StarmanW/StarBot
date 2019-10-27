from discord.ext import commands
from cogs.cog import StarPyCog


class Fun(StarPyCog):
    def __init__(self, client):
        super(Fun, self).__init__(client)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello there, {ctx.author.mention}!")

    @commands.command()
    async def coin(self, user_choice):
        pass

    @commands.command()
    async def rps(self, user_choice):
        pass

def setup(client):
    client.add_cog(Fun(client))
