import json

with open('config/caller.json', 'r') as config_file:
    config = json.load(config_file)

with open('config/private.key', 'r') as key_file:
    private_key = key_file.read()
