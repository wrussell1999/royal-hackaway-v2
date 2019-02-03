import os
import json
from pprint import pprint

import flask
from flask import Flask, request, jsonify

from . import voice

def main():
    app = Flask(__name__)

    themes = {}

    @app.route('/webhooks/inbound_sms', methods=['GET', 'POST'])
    def inbound_sms():
        if request.is_json:
            pprint(request.get_json())
        else:
            data = dict(request.form) or dict(request.args)
            mobile_number = data['msisdn']
            themes[mobile_number] = data['text'].split(' ')[-1]
            print('User number: ' + mobile_number)
            print('Theme: ' + themes[mobile_number])
            voice.make_call(mobile_number)

        return ('', 204)

    @app.route('/calls/<number>.json')
    def send(number):
        return flask.jsonify([
            {
                "action": "talk",
                "voiceName": "Brian",
                "text": themes[number]
            }
        ])

    app.run(port=3000)
