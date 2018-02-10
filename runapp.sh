#!/usr/bin/env sh

cd web/app
pip3 install requests==2.18.4
pip3 install Flask==0.12.2
pip3 install tweepy==3.5.0
pip3 install spotipy==2.4.4

python3 app.py
