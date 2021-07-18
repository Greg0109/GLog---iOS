#!/usr/bin/env python3
from flask import Flask, request
import base64
import logging
import sys

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    if 'GLog' in request.json:
        base64received = request.json['GLog']
        base64decodereceived = base64.b64decode(base64received)
        text = base64decodereceived.decode('UTF-8')
        print('%s' % text)
    return '\n'

def runServer(port):
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    runServer(port)
