from utils import getlinks
import requests
from bs4 import BeautifulSoup


def web_parser(site_lists, selected_website, options):
    if selected_website == 'digikala':
        for site in site_lists:
            response = requests.get(site)
            soup = BeautifulSoup(response.text, "html.parser")
            pricediv = soup.find_all("div", {"c-product__seller-price-pure js-price-value"})
            titlediv = soup.find_all("h1", {"c-product__title"})
            if len(pricediv) == 0:
                return 'ناموجود', titlediv[0].contents[0].strip()
            else:
                return pricediv[0].contents[0], titlediv[0].contents[0].strip()