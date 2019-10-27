from os import walk
from time import time
from os.path import abspath
from discord.ext import commands
import re

# Function for blocking DMs globally
async def globally_block_dms(ctx):
    return ctx.guild is not None
    
class StarPy(commands.Bot):
    def initialize(self, config):
        self.uptime = time()
        self.config = config
        self.prefix = self.config['prefix']
        self.initialize_cogs()
        self.initialize_check()
        self.run(self.config['token'])

    def initialize_cogs(self):
        for (_, _, files) in walk(abspath(self.config['cogs_directory'])):
            for f in files:
                if (f[:-3] != 'cog') and not f.endswith('.pyc'):
                    self.load_extension(f'{self.config["cogs_directory"][2:]}.{f[:-3]}')

    def initialize_check(self):
        self.add_check(globally_block_dms)

        