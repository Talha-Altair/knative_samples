from flask import *
import requests
from dotenv import load_dotenv
import os

PORT = os.environ.get('PORT')
BACKEND_URL = os.environ.get('BACKEND_URL')

app = Flask(__name__)

@app.route("/")
def home():

    return render_template('index.html')

@app.route("/add")
def add():

    a = request.form.get('a')
    b = request.form.get('b')

    data = {
        "a" : a,
        "b" : b
    }

    req = requests.post(url = BACKEND_URL + '/add', json = data)

    res = req.json.get('sum')

    return render_template('index.html', ans = res)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=PORT)