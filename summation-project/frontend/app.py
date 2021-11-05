from flask import *
import requests

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

    req = requests.post(url=)

    return render_template('index.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8500)