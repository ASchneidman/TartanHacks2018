from flask import Flask, render_template, jsonify, send_from_directory
import requests
from twitterAPI import get_tweets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_local/<coords>')
def get_path(coords):
    print (coords)
    arr = coords.split(',')
    result = get_tweets(arr[0], arr[1], 10)
    return (str(result))

def main():
    app.run(host='0.0.0.0')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    main()
