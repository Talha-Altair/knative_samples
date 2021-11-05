from flask import *
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

PORT = os.environ.get('PORT')
BACKEND_URL = os.environ.get('BACKEND_URL')

app = Flask(__name__)

@app.route("/")
def home():

    return render_template('index.html')

@app.route("/add", methods = ['GET','POST'])
def add():

    a = request.form.get('a')
    b = request.form.get('b')

    data = {
        "a" : int(a),
        "b" : int(b)
    }

    req = requests.post(url = BACKEND_URL + '/add', json = data)

    res = json.loads(req.content)

    res = res['sum']

    return render_template('result.html', ans = res)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=PORT)