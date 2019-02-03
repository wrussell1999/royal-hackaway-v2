import nexmo
from pprint import pprint

from . import config

client = nexmo.Client(
    application_id=config.config['APPLICATION_ID'],
    private_key=config.private_key,
)

def make_call(number):
    server = config.config['SERVER']
    client.create_call({
        'to': [
            {
                'type': 'phone',
                'number': number
            }
        ],
        'from': {
            'type': 'phone',
            'number': config.config['NEXMO_NUMBER']
        },
        'answer_url': [
            f'{server}/calls/{number}.json'
        ]
    })
