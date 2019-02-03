import nexmo
import json

with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)

client = nexmo.Client(key=config['APPLICATION_ID'], secret=config['SECRET'])
print(client.send_message({'from': 'Royal Hackaway', 'to': config['TO_NUMBER'], 'text': 'Test message'}))