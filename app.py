from flask import Flask, session, request, send_from_directory, jsonify
import yaml
import sqlite3

# Consider replacing some useage of random with cryptograhic secure secrets
from random import randint
from secrets import token_bytes
import os
from base64 import b64encode
from hashlib import sha256

# Load clues.json into memory
with open('clues.yml', 'r') as file:
    clues = yaml.safe_load(file)
print(clues)
quit()
IMAGE_DIR = os.path.join(os.path.dirname(__file__), "images/")


app = Flask(__name__)

# Secret key generated at runtime. 
app.secret_key = token_bytes(64)


@app.route('/')
def index():
    return '<p>Hello there!</p>'


@app.route('/new_session')
def newSession():
    session['results'] = []
    session['image_hashes_seen'] = []



@app.route('/uniguessur/random_clue')
def getRandomClue():
    clue = clues[randint(0, len(clues)-1)]
    while clue['hash'] in session['image_hashes_seen']:
        clue = clues[randint(0, len(clues)-1)]
    
    session['image_hashes_seen'].append(clue['hash'])

    with open(IMAGE_DIR, clue['filename']) as image:
        b64_image = base64encode(f.read()).decode('ascii')

    return jsonify({
        'image': f'data:image/jpeg;base64,{b64_image}',
        'credit': clue['credit'],
        'subject_x': clue['subjects']['x'],
        'subject_y': clue['subjects']['y']
    })


if __name__ == '__main__':
    app.run(port=4000)