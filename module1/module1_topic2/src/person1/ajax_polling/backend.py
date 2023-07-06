import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/state', methods=['GET'])
def get_state():
    state = get_state_from_db() 
    response = jsonify(state)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def get_state_from_db():
    with open('database.json', 'r') as db:
        state = json.load(db)
    return state

if __name__ == '__main__':
    app.run()
