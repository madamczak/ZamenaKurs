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
    address_div = soup.find('div', {"class": "oglField--address"})
    district_div = address_div.find('div', {"class": "oglField__container"})
    address = district_div.text.replace("Adres", "")
    return address
#D
def parse_price_square_meter(soup):
    pass

def parse_building_year(soup):
    building_year_div = soup.find('div', {"class": "oglField--rok_budowy"})
    building_year_span = building_year_div.find('span', {"class": "oglField__value"})
    building_year = int(building_year_span.text)
    return building_year

# P
def parse_area(soup):
    area_div = soup.find('div', {"id": "show-powierzchnia"})
    area_span = area_div.find('span', {"class": "oglField__value"})
    area = float(area_span.text)
    return area
# D
def parse_floor(soup):
    pass
# P
def parse_building_type(soup):
    building_type_div = soup.find('div', {"class": "oglField--rodzaj_nieruchomosci"})
    building_type_span = building_type_div.find('span', {"class": "oglField__value"})
    building_type = building_type_span.text.lower()
    return building_type
#D
def parse_heating_type(soup):
    pass
#P
def parse_number_of_rooms(soup):
    number_of_rooms_div = soup.find('div', {"class": "oglField--l_pokoi"})
    number_of_rooms_span = number_of_rooms_div.find('span', {"class": "oglField__value"})
    number_of_rooms = int(number_of_rooms_span.text)
    return number_of_rooms
#D
def parse_building_floors(soup):
    pass


link="https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html"
soup=get_soup(link)

print(parse_area(soup))
# print(parse_price(soup))

# "REAL_ESTATE" = {
#     "price": int,
#     "address": text,
#     "square_meter_price": float,
#     "building_year": int,
#     ...
# }
