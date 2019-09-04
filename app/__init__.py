from flask import Flask, request, jsonify
import subprocess, uuid, os
import logging, time
import json
import pprint
from io import StringIO
import sys
app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.before_first_request
def serveo_forward():
    id = str(uuid.uuid4()).split('-')[0]
    domain = "webhooks_{}.serveo.net".format(id)
    FNULL = open(os.devnull, 'w')
    p = subprocess.Popen(['ssh', '-R', '{}:80:127.0.0.1:5000'.format(domain), 'serveo.net'], stdout=FNULL, stderr=subprocess.STDOUT)
    print('')
    print('WEBHOOK URL: https://%s' % domain)
    print('PRESS CRTL+C TWICE TO QUIT')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        webhook = request.json
        print('<<<< WEBHOOK >>>>')
        print('\r')
        print(json.dumps(webhook))
        print('\r')
        print('<<<<   END   >>>>')
        print('\r')
        return jsonify('Thanks!')
    else:
        return jsonify('Webhook Running, Check Console For Webhook URL')
