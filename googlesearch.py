import requests
from utils import getlinks
class googlesearch:
    def __init__(self):
        self.prefixurl = 'https://www.google.com/search?q='

    def crawl(self, searchtext):
        response = requests.get(self.prefixurl+searchtext)
        links = getlinks.getlinks(response.text, "^/url\?q=https://www.digikala.com/product/")
        # need to review
        linkslist = []
        for link in links:
            link = link.split('/url?q=')
            linkslist.append(link[1])
        return linkslist





