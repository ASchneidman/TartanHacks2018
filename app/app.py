from flask import Flask, render_template, jsonify, send_from_directory
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def main():
    app.run(host='0.0.0.0')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    main()
