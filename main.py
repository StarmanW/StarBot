# Import bot
from modules.client import StarPy
import modules.utils as utils
 
# Read config file and create bot instance
config = utils.read_config_file()
bot = StarPy(config['prefix'])
bot.initialize(config)
