#!/bin/python

from bs4 import BeautifulSoup
import requests

page = 'https://en.wikipedia.org/wiki/Most_common_words_in_English'
r = requests.get(page)
soup = BeautifulSoup(r.content, 'html.parser')

body = soup.find('body')
content1 = body.find('div', {'id': 'bodyContent'})
content2 = content1.find('div', {'id': 'mw-content-text'})
content3 = content2.find('div', {'class': 'mw-parser-output'})
tbody = content3.find('table').find('tbody')
entries = tbody.find_all('tr')
words = [e.find('td').find('a').text for e in entries[1:]]

with open('100commonwords.txt', 'w+') as f:
    for word in words:
        if len(word) > 1:
            f.write(f'{word.lower()}\n')
