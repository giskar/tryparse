
from bs4 import BeautifulSoup
import urllib.request
import json

html_doc =  urllib.request.urlopen('http://pikabu.ru/').read()
soup = BeautifulSoup(html_doc, "html.parser")


a = soup.find('div', 'story')
feeds=[]
while True:
    try:
        b = a.find('a', 'story__author').get_text()
        c = a.find('div', 'story__tags').get_text()
        d = a.find('a').get('href')
        e = a.find('a').get_text(strip=True)
        t = a.find('div', 'story__rating-count').get_text(strip=True)
        a = a.find_next('div', 'story')
        data = {
        'author': b,
        'tags': c.split( ),
        'link': d,
        'name': e,
        'rate': t
        }
        feeds.append(data)

    except: break

print(feeds)
with open('JSONData.json', 'w') as f:
     json.dump(feeds, f)