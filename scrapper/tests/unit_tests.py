from ..trojmiasto.website_parser import parse_price, get_soup

assert parse_price(get_soup(
    "https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html")) == 239000

assert parse_price(get_soup("https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-pierwotny/mieszkanie-b32-sw-piotra-87-00m2-ogl64079118.html")) == 1399840
