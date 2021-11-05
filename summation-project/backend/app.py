from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)

PORT = os.environ.get('PORT')

@app.route("/add")
def add():

    a = request.json.get('a')

    b = request.json.get('b')

    res = {
        "sum" : a + b
    }

    return jsonify(res)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=PORT)