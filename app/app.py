from flask import Flask, render_template, jsonify, send_from_directory
import requests
import re
from twitterAPI import get_tweets
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_local/<coords>')
def get_path(coords):
    print (coords)
    arr = coords.split(',')
    result = get_tweets(arr[0], arr[1], 20)
    result1 = []
    print(str(result))
    bycount = 0
    for tweet in result:
        tweeter = tweet.split(' ')
        if "by" in tweeter:
            bycount += 1
            result1.append(re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("by")+1]))))
<<<<<<< HEAD
            print (bycount)
            #if tweeter.index("by")+2 < len(tweeter):
                #result1[len(result1)-1] += ' ' + re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("by")+2])))
=======

        elif "#NowPlaying" in tweeter:
            result1.append(re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("#NowPlaying")+1]))))
            if tweeter.index("#NowPlaying")+2 < len(tweeter):
                result1[len(result1)-1] += ' ' + re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("#NowPlaying")+2])))
>>>>>>> f584316e96497eff8875fedbd6e864e781d67bee
    result1 = list(set(result1))
            #result1.append(tweeter[tweeter.index("by")+2])
    return (str(result1))

def main():
    app.run(host='0.0.0.0')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    main()
