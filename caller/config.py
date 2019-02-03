import json

with open('caller/config/config.json', 'r') as config_file:
    config = json.load(config_file)

with open('caller/config/private.key', 'r') as key_file:
    private_key = key_file.read()
