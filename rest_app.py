from db_connector import *
from flask import Flask, request
import os
import signal

app = Flask(__name__)

@app.route('/users/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])

def user(id):
    if request.method == 'POST':
        try:

            name = request.json.get('name')
            set_data(id, name)
            return {'status': 'ok', 'user added': name}, 201  # status code
        except:
            return {'status': 'error', 'reason': f"ID {id} already exists"}, 500  # status code

    elif request.method == 'GET':
        try:
            name = get_data(id)
            if name:
                return {'status': 'ok', 'name': name}, 200
            else:
                raise Exception
        except:
            return {'status': 'error', 'reason': "No such id"}, 500  # status code

    elif request.method == 'PUT':
        try:

            name = request.json.get('name')
            update(id, name)
            return {'status': 'ok', 'user_updated': name}, 200  # status code
        except:
            return {"status": "error", "reason": "No such id"}, 500

    elif request.method == 'DELETE':
        try:
            remove(id)
            return {'status': 'ok', 'user_deleted': id}, 200  # status code
        except:
            return {'status': 'error', 'reason': "Mo such id"}, 500

@app.route('/stop_server',methods=['GET'])
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'

@app.route('/')
def health():
    return '200'

app.run(host='0.0.0.0', port=5000)
