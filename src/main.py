from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/swapi/<category>/', defaults={'id': None})
@app.route('/swapi/<category>/<int:id>')
def swapi(category, id):
    if category not in ['films', 'people', 'planets', 'species', 'starships', 'vehicle'] or (id is not None and id < 1):
        return error()
    swapi_url = f"https://swapi.dev/api/{category}/"
    if id is not None:
        swapi_url += f"{id}/"
    data = None
    response = requests.get(swapi_url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
    else:
        return error()
    return render_template('index.html', data=data)


def error():
    return render_template('index.html', data={
        "code": 404,
        "message": "Not Found"
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
