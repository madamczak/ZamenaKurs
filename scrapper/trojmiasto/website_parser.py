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
    price_square_meter_div = soup.find('div', {"class": "oglField oglField--cena_za_m2"})
    price_square_meter_span = price_square_meter_div.span.find(text=True, recursive=False)
    price_square_meter = int(price_square_meter_span.replace(" ", ""))
    return price_square_meter

def parse_building_year(soup):
    building_year_div = soup.find('div', {"class": "oglField--rok_budowy"})
    building_year_span = building_year_div.find('span', {"class": "oglField__value"})
    building_year = int(building_year_span.text)
    return building_year

#P
def parse_area(soup):
    pass
#D
def parse_floor(soup):
    floor_div = soup.find('div', {"class": "oglField oglField--pietro"})
    floor_span = floor_div.find('span', {"class": "oglField__value"})
    floor = int(floor_span.text)
    return floor
#P
def parse_building_type(soup):
    pass
#D
def parse_heating_type(soup):
    heating_type_div = soup.find('div', {"class": "oglField oglField--typ_ogrzewania"})
    heating_type_span = heating_type_div.find('span', {"class": "oglField__value"})
    heating_type = heating_type_span.text
    return heating_type
#P
def parse_number_of_rooms(soup):
    pass
#D
def parse_building_floors(soup):
    building_floors_div = soup.find('div', {"class": "oglField oglField--l_pieter"})
    building_floors_span = building_floors_div.find('span', {"class": "oglField__value"})
    building_floors = int(building_floors_span.text)
    return building_floors

link="https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html"
soup=get_soup(link)

print(parse_price_square_meter(soup))
print(parse_floor(soup))
print(parse_heating_type(soup))
print(parse_building_floors(soup))
# print(parse_price(soup))

# "REAL_ESTATE" = {
#     "price": int,
#     "address": text,
#     "square_meter_price": float,
#     "building_year": int,
#     ...
# }
