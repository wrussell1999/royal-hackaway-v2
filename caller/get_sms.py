import os
import json
from pprint import pprint

import flask
from flask import Flask, request, jsonify
from flask import url_for

from . import voice
from . import tts_json

def main():
    app = Flask(__name__)
    @app.route('/webhooks/inbound_sms', methods=['GET', 'POST'])
    def inbound_sms():
        if request.is_json:
            pprint(request.get_json())
        else:
            data = dict(request.form) or dict(request.args)
            theme = data['text'].split(' ')[-1]
            mobile_number = data['msisdn']
            print('Theme: ' + theme)
            print('User number: ' + mobile_number)
            tts_json.insert_lyric(theme)
            voice.make_call(mobile_number)
        return ('', 204)

    @app.route('/data.json')
    def send():
        filename = os.path.abspath('data.json')
        return flask.send_file(filename)

    app.run(port=3000)
