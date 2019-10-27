import json
import os

# Decorator to check configuration file
def config_file_check(func):
    def is_file_exist():
        if (os.path.isfile('./config.json')):
            return func()
        else:
            raise Exception("Configuration file not found.")
    return is_file_exist

# Read configuration file
@config_file_check
def read_config_file():
    with open('./config.json', 'r') as configFile:
        data = json.load(configFile)
    return data