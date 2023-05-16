from flask import Flask, render_template, jsonify, request
from service import processar
import json
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    content = request.json

    return jsonify(json.loads(json.dumps(processar(content))))


if __name__ == '__main__':
    app.run()
