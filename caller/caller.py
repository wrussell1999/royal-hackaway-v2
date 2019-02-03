import os
import json
from pprint import pprint
from . import text_to_mp3

import flask
from flask import Flask, request, jsonify

from . import config
from . import voice

from . import lyrics

import threading

from collections import deque
import uuid

clips = {}

def main():
    app = Flask(__name__)

    songs = lyrics.load_songs()
    gen = lyrics.Generator(songs)

    @app.route('/webhooks/inbound_sms', methods=['GET', 'POST'])
    def inbound_sms():
        if request.is_json:
            pprint(request.get_json())
        else:
            data = dict(request.form) or dict(request.args)
            mobile_number = data['msisdn']
            theme = data['text'].split(' ')[-1]

            print('User number: ' + mobile_number)
            print('Theme: ' + theme)

            tosend = gen.generate_lyrics(theme)

            thread = threading.Thread(target=lambda: make_call(tosend, mobile_number))
            thread.start()

        return ('', 204)

    @app.route('/calls/<number>.json')
    def send(number):
        print(f'Calling to {number}')
        server = config.config['SERVER']

        recording = clips[number].popleft()
        recording = os.path.basename(recording)

        if os.path.exists(os.path.join('cache/recordings/', recording)):
            print("RETURNING AUDIO")
            recording = f'{server}/recordings/{recording}'
            return flask.jsonify([
                {
                    'action': 'stream',
                    'level': 1,
                    'streamUrl': [recording]
                }
            ])
        else:
            return flask.jsonify([
                {
                    'action': 'talk',
                    'text': 'Error: could not find recording'
                }
            ])

    @app.route('/recordings/<filename>')
    def get_recording(filename):
        path = os.path.abspath('cache/recordings')
        return flask.send_from_directory(path, filename, cache_timeout=-1)

    app.run(port=3001)

def make_call(text, mobile_number):
    filename = f"cache/recordings/{mobile_number}-{uuid.uuid4()}.mp3"
    filename = text_to_mp3.make_mp3(text, filename)
    if mobile_number in clips:
        clips[mobile_number].append(filename)
    else:
        clips[mobile_number] = deque([filename])
    voice.make_call(mobile_number)
