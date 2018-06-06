from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

app=Flask(__name__)

@app.route('/home')
def index():
    r=requests.get("http://www.metrolyrics.com/top100.html")
    soup=BeautifulSoup(r.text,"html.parser")
    song=soup.findAll("a",{"class":"song-link hasvidtoplyric"})
    songs=[]
    for x in song:
        songs.append(x.text)
    links=[]
    for y in song:
        links.append(y['href'])
    return render_template('index.html', songs=songs, links=links)

if __name__=='__main__':
    app.jinja_env.globals.update(zip=zip)
    app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
