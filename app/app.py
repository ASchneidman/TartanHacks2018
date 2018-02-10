from flask import Flask, render_template, jsonify, send_from_directory
import requests
from twitterAPI import get_tweets
import re
#import nltk
#from nltk.tag.stanford import StanfordNERTagger
#st = StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
'''
def extract_entities(text):

    for sent in nltk.sent_tokenize(text):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            if tag[1]=='PERSON': print (tag)

    for sent in nltk.sent_tokenize(text):
         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'node'):
                print (chunk.node, ' '.join(c[0] for c in chunk.leaves()))
'''

@app.route('/get_local/<coords>')
def get_path(coords):
    print (coords)
    '''
    arr = coords.split(',')
    result = get_tweets(arr[0], arr[1], 10)
    print (str(result))
    return ("Got em")
'''
    arr = coords.split(',')
    result = get_tweets(arr[0], arr[1], 20)
    result1 = []
    for tweet in result:
        tweeter = tweet.split(' ')
        if "by" in tweeter:
            result1.append(re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("by")+1]))))
            #if tweeter.index("by")+2 < len(tweeter):
                #result1[len(result1)-1] += ' ' + re.sub('stco*','',re.sub('http*','',re.sub('[^A-Za-z0-9]+','',tweeter[tweeter.index("by")+2])))
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
