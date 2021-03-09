from bs4 import BeautifulSoup
import requests


def get_soup(url):
    agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    if not (url.startswith("http://") or url.startswith("https://")):
        return "Incorrect url."

    url_get = requests.get(url, headers=agent)
    response_code = str(url_get.status_code)

    if not (response_code.startswith("2") or response_code.startswith("3")):
        return "Error response code (" + response_code + ")."

    soup = BeautifulSoup(url_get.text, "lxml")

    return soup


def parse_price(soup):
    price_span = soup.find('span', {"class": "oglDetailsMoney"})
    price_output = (price_span.contents.pop(0))
    price = int(price_output.replace(" ", ""))
    return price


def parse_address(soup):
    pass

def parse_price_square_meter(soup):
    pass

def parse_building_year(soup):
    pass

def parse_area(soup):
    pass

def parse_floor(soup):
    pass

def parse_building_type(soup):
    pass

def parse_heating_type(soup):
    pass

def parse_number_of_rooms(soup):
    pass

def parse_building_floors(soup):
    pass


# "REAL_ESTATE" = {
#     "price": int,
#     "address": text,
#     "square_meter_price": float,
#     "building_year": int,
#     ...
# }
