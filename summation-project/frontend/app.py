from flask import Flask, jsonify
from faker import Faker

fake = Faker()

app = Flask(__name__)

@app.route("/")
def hello_world():

    city = fake.city()

    res = {
        "city" : city
    }

    return jsonify(res)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8500)