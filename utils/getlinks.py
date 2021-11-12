from bs4 import BeautifulSoup
import re

def getlinks(content,pattern):
    bs = BeautifulSoup(content,"html.parser")
    urllists = bs.findAll('a', attrs={'href': re.compile(pattern)})
    href = []
    for url in urllists:
        href.append(url.get('href'))
    href = set(href)
    return href