import os
import json
from pprint import pprint

import flask
from flask import Flask, request, jsonify

from . import config
from . import voice

def main():
    app = Flask(__name__)

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

            # TODO: generate recording here in recordings/{number}.mp3

            voice.make_call(mobile_number)

        return ('', 204)

    @app.route('/calls/<number>.json')
    def send(number):
        server = config.config['SERVER']
        recording = f'{server}/recordings/{number}.mp3'

        if True:
        # if os.path.exists(f'recordings/{number}.mp3')
            return flask.jsonify([
                {
                    'action': 'stream',
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

    @app.route('/recordings/<path:filename>')
    def get_recording(filename):
        path = os.path.abspath('output.mp3')
        return flask.send_file(path)
        # path = os.path.abspath('cache/recordings/')
        # return flask.send_from_directory(path, filename)

    app.run(port=3000)
