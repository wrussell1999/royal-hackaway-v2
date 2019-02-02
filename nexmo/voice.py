import nexmo
import json
from pprint import pprint

with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)

with open('config/private.key', 'r') as key_file:
    private_key = key_file.read()

client = nexmo.Client(
    application_id=config['APPLICATION_ID'],
    private_key=private_key,
)

response = client.create_call({
  'to': [{'type': 'phone', 'number': config['TO_NUMBER']}],
  'from': {'type': 'phone', 'number': config['NEXMO_NUMBER']},
  'answer_url': ['https://ff31a71a.ngrok.io/data.json']
})

pprint(response)
