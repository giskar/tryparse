
from bs4 import BeautifulSoup
import urllib.request
import json

html_doc =  urllib.request.urlopen('http://pikabu.ru/').read()
soup = BeautifulSoup(html_doc, "html.parser")


story = soup.find('div', 'story')
feeds=[]
while True:
    try:
        author = story.find('a', 'story__author').get_text()
        tags = story.find('div', 'story__tags').get_text()
        link = story.find('a').get('href')
        name = story.find('a').get_text(strip=True)
        rate = story.find('div', 'story__rating-count').get_text(strip=True)
        story = story.find_next('div', 'story')
        data = {
        'author': author,
        'tags': tags.split( ),
        'link': link,
        'name': name,
        'rate': rate
        }
        feeds.append(data)

    except: break

print(feeds)
with open('JSONData.json', 'w') as f:
     json.dump(feeds, f)