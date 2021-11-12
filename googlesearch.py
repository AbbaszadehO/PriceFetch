import requests
from utils import getlinks
class googlesearch:
    def __init__(self):
        self.prefixurl = 'https://www.google.com/search?q='

    def crawl(self, searchtext, selected_website):
        response = requests.get(self.prefixurl+searchtext)
        links = getlinks.getlinks(response.text, "^/url\?q=https://www."+selected_website+".com/product/")
        # ToDo
        linkslist = []
        for link in links:
            link = link.split('/url?q=')
            linkslist.append(link[1])
        return linkslist





