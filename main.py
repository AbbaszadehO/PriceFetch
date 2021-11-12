import json
import pandas as pd
from googlesearch import googlesearch
from yahoosearch import yahoosearch



if __name__ == '__main__':
    f = open('config.json')
    config = json.load(f)
    input_products =  pd.read_excel(config["inputlist"])
    input_products = input_products['نام کالا']
    searchengines = config['search_engine']
    for searchengine in searchengines:
        if searchengine == 'google':
            g = googlesearch()
            g.crawl('موبایل شیائومی نوت ۱۰')
        # elif searchengine == 'yandex':
        #     y = yandexsearch()
        # elif searchengine == 'yahoo':
        #     y = yahoosearch()
        # elif searchengine == 'torch':
        #     y = torchsearch()
