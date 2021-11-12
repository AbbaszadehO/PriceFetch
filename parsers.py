from utils import getlinks
import requests

def web_parser(site_lists, selected_website, options):
    if selected_website == 'digikala':
        for site in site_lists:
            requests.get(site)