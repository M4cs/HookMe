from flask import Flask, request, jsonify
import subprocess, uuid, os
import logging, time
import json
import pprint
from fabulous.color import *
from io import StringIO
import sys, subprocess
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        webhook = request.data
        print(green(bold('<<<< WEBHOOK >>>>')))
        print('\r')
        buf = StringIO(json.dumps(json.loads(webhook), indent=4))
        for line in buf.readlines():
            print('\r' + line.replace('\n', ''))
        print('\r')
        print(green(bold('<<<<   END   >>>>')))
        print('\r')
        return jsonify('Thanks!')
    else:
        return jsonify('Webhook Running, Check Console For Webhook URL')
