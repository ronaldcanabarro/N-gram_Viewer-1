from flask import Flask, render_template, jsonify, request
from random import randint
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    #ler o arquivo
    #counterizar
    #qualquercoisas

    CHART = {
            "labels": ["2017", "2018"],
            "dataset": [{
                "label": "ana",
                "data": [1, 2]
            },
                {
                    "label": "Luciano",
                    "data": [2, 1]
                }
            ]
        }

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    content = request.json

    LABELS = [randint(1997, 2020) for i in range(len(content))]

    DATASET = []

    for l in content:
        data = {}
        data['label'] = l
        data['data'] = [randint(0, 20) for i in range(len(content))]
        DATASET.append(data)

    CHART = {
            "labels": LABELS,
            "dataset": DATASET
        }

    return jsonify(CHART)


if __name__ == '__main__':
    app.run()
