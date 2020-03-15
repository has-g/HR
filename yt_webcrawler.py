# https://www.youtube.com/watch?v=sVNJOiTBi_8
import requests
from bs4 import BeautifulSoup

def wikicrawler(max_size = 0):
    url = 'https://en.wikipedia.org/wiki/Inter-process_communication'
    html_text = requests.get(url)
    plain_text = html_text.text
    soup = BeautifulSoup(plain_text)

    for link in soup.findAll('a', {'class': 'portal'}):
        href = link.get('href')
        print(href)

wikicrawler()