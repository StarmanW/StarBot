from time import time
import datetime
from discord.ext import commands
from discord import Embed, Colour
from cogs.cog import StarPyCog


class Core(StarPyCog):
    def __init__(self, client):
        super(Core, self).__init__(client)

    @commands.command(aliases=['sh', 'shut'])
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Bot shutting down...')
        await self.client.logout()

    @commands.command(aliases=['clr', 'cl'])
    async def clean(self, ctx, limit=20):
        # Permission check
        if (ctx.author.permissions_in(ctx.channel).manage_messages != True): return
        if (ctx.me.permissions_in(ctx.channel).manage_messages != True):
            return await ctx.send('I do not have the permission to manage message :slight_frown:')

        # Retrieve messages
        messages = await ctx.channel.history(limit=(100 if limit > 100 else limit)).flatten()
        if (len(messages) <= 1): return

        # Delete messages
        await ctx.channel.delete_messages(messages)
        await ctx.send(f'Successfully deleted {len(messages) - 1} message(s).', delete_after=5)

    @commands.command()
    async def uptime(self, ctx):
        # Calculate uptime
        difference = int(round(time() - self.client.uptime))
        text = str(datetime.timedelta(seconds=difference))

        # Create embed for uptime
        embed = Embed(colour=Colour(0xFF0101))
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="**Bot Uptime**", value=text)
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx):
        pass

    @commands.command()
    async def serverinfo(self, ctx):
        pass

    @commands.command(aliases=['rldex'])
    @commands.has_permissions(administrator=True)
    async def reloadext(self, ctx, ext=None):
        if ext is not None:
            self.client.reload_extension(f'{self.client.config["cogs_directory"][2:]}.{ext}')
            return await ctx.send(f'Successfully reloaded {ext}.')

        for e in self.client.extensions.keys():
            self.client.reload_extension(e)
        return await ctx.send(f'Successfully reloaded {len(self.client.extensions)} extensions.')

    @commands.command(aliases=['ldex'])
    @commands.has_permissions(administrator=True)
    async def loadext(self, ctx, ext=None):
        if ext is None:
            return await ctx.send('Please specify an extension to load.')
        self.client.load_extension(f'{self.client.config["cogs_directory"][2:]}.{ext}')
        await ctx.send(f'Successfully loaded {ext}.')

    @commands.command(aliases=['uldex'])
    @commands.has_permissions(administrator=True)
    async def unloadext(self, ctx, ext=None):
        if ext is None:
            return await ctx.send('Please specify an extension to unload.')
        if ext == 'core':
            return await ctx.send('Core extension are not allowed to be unloaded.')

        self.client.unload_extension(f'{self.client.config["cogs_directory"][2:]}.{ext}')
        await ctx.send(f'Successfully unloaded {ext}.')

def setup(client):
    client.add_cog(Core(client))
