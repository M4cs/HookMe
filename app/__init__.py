from flask import Flask, request, jsonify, render_template
import subprocess, uuid, os
import logging, time
import json
import pprint
from io import StringIO
import sys, subprocess
app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/trisha', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        webhook = request.data
        with open('app/templates/trisha.html', 'r+') as trisha:
            trisha.truncate()
            trisha.seek(0)
            trisha.write(f"""\
=============== WEBHOOK =============
{json.dumps(webhook, indent=4)}
================= END ===============

""")
            trisha.close()
    else:
        return render_template('trisha.html')


@app.route('/max', methods=['POST', 'GET'])
def max_hook():
    if request.method == 'POST':
        webhook = request.data
        with open('app/templates/max.html', 'r+') as trisha:
            trisha.truncate()
            trisha.seek(0)
            trisha.write(f"""\
=============== WEBHOOK =============
{json.dumps(webhook, indent=4)}
================= END ===============

""")
            trisha.close()
    else:
        return render_template('max.html')