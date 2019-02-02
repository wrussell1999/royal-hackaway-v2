import nexmo
from pprint import pprint
import json

with open("config.json") as file:
    config = json.load(file)

client = nexmo.Client(
    application_id=config['APPLICATION_ID'],
    private_key=config['APPLICATION_PRIVATE_KEY_PATH'],
)

response = client.create_call({
  'to': [{'type': 'phone', 'number': config['TO_NUMBER']}],
  'from': {'type': 'phone', 'number': config['NEXMO_NUMBER']},
  'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
})

pprint(response)