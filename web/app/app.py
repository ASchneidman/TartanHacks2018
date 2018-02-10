from flask import Flask, render_template, jsonify, send_from_directory
import requests
import re
from twitterAPI import get_tweets
from spotifyAPI import get_tracks
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/loader.html')
def load():
    return render_template('loader.html')

@app.route('/get_local/<coords>')
def get_path(coords):
    print (coords)
    arr = coords.split(',')
    result = get_tweets(arr[0], arr[1], 20)
    #username = arr[2]
    result1 = []
    print(str(result))
    for tweet in result:
        tweeter = tweet.split(' ')
        if "by" in tweeter:
            result1.append(re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("by")+1]))))

        elif "#NowPlaying" in tweeter:
            result1.append(re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("#NowPlaying")+1]))))
            if tweeter.index("#NowPlaying")+2 < len(tweeter):
                result1[len(result1)-1] += ' ' + re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("#NowPlaying")+2])))

    result1 = list(set(result1))
            #result1.append(tweeter[tweeter.index("by")+2])
    playlistid = get_tracks(result1)
    return render_template('album.html',value=playlistid,location=coords)

def main():
    app.run(host='0.0.0.0')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    main()
