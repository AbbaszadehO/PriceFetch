# -*- coding: utf-8 -*-
import json
import pandas as pd
from googlesearch import googlesearch
from yahoosearch import yahoosearch
from yandexsearch import yandexsearch
import parsers


if __name__ == '__main__':
    with open('config.json', encoding='utf-8') as fh:
        config = json.load(fh)
    input_products = pd.read_excel(config["inputlist"])
    input_products = input_products['نام کالا']
    searchengines = config['search_engine']
    selected_websites = config['selected_websites']
    options = config['options']
    for searchengine in searchengines:
        for product in input_products:
            if searchengine == 'google':
                g = googlesearch()
                for selected_website in selected_websites:
                    site_lists = g.crawl(product, selected_website)
                    if len(site_lists) == 0 :
                        continue
                    else:
                        reults = parsers.web_parser(site_lists=site_lists,
                                            selected_website=selected_website,
                                            options=options)

            elif searchengine == 'yandex':
                y = yandexsearch()
            elif searchengine == 'yahoo':
                y = yahoosearch()
            # elif searchengine == 'torch':
            #     y = torchsearch()
