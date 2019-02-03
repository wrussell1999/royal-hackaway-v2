import nexmo
import json
from pprint import pprint

with open('caller/config/config.json', 'r') as config_file:
    config = json.load(config_file)

with open('caller/config/private.key', 'r') as key_file:
    private_key = key_file.read()

print(dir(nexmo))
client = nexmo.Client(
    application_id=config['APPLICATION_ID'],
    private_key=private_key,
)

def make_call(number):
    client.create_call({
        'to': [{'type': 'phone', 'number': number}],
        'from': {'type': 'phone', 'number': config['NEXMO_NUMBER']},
        'answer_url': ['https://d17bbcee.ngrok.io/data.json']
    })
