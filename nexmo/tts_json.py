import json

with open('data.json', 'r') as data_file:
    data = json.load(data_file)

def insert_lyric(lyric):
    data[0]['text'] = lyric
    save_to_json()

def save_to_json():
    with open('data.json', 'w') as data_file:
        json.dump(data, data_file)


insert_lyric("Rap god")