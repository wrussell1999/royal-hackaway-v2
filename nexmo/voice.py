import nexmo
from pprint import pprint

with open('config.json', 'r') as config_file:
    config = config_file.read()

with open('private.key', 'r') as content_file:
    content = content_file.read()

client = nexmo.Client(
    application_id=config['APPLICATION_ID'],
    private_key=content,
)


response = client.create_call({
  'to': [{'type': 'phone', 'number': config['TO_NUMBER']}],
  'from': {'type': 'phone', 'number': config['NEXMO_NUMBER']},
  'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
})

pprint(response_text)