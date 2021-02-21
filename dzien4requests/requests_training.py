import requests

link = "https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html"

agent = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
import time

now = time.time()
page = requests.get(link, headers=agent)

# print(page.text)
# print(time.time() - now)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.text, "lxml")

# print(soup)

all_divs = soup.find_all('div', {"class" : "oglDetails panel"})

# for element in all_divs:
#     span_elem = element.find_all("span")
#     for span in span_elem:
#         print(span.text)


flat_dict1 = {"cena": 239000, "cena_za_metr": 8852, "rok": 1980}
flat_dict2 = {"cena": 40000, "cena_za_metr": 312312123, "rok": 1985}
flat_dict3 = {"cena": 6783126897123, "cena_za_metr": 423432423, "rok": 1990}

lista_mieszkan = [flat_dict1, flat_dict2, flat_dict3]

suma = 0


for flat in lista_mieszkan:
    rok = flat.get("rok")
    print("rok:", rok)
    suma += rok

print(suma/len(lista_mieszkan))
