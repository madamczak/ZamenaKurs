#napisz funkcję która jako argument przyjmie stringa url, sprawdzi czy string rozpoczyna się od http:// lub https://
#następnie wykona request typu get, sprawdzi czy kod odpowiedzi zaczyna się na 2(OK) lub 3(Przekierowanie)
#i dalej już tylko utworzy obiekt BeautifulSoup, jako argumenty do budowy obiektu podasz tekst strony a jako parser "lxml"
#i na końcu zwróci go z funkcji
#w każdym kroku sprawdzającym możesz uznać że jeżeli warunek nie jest spełniony to możesz od razu ją przerwać i zwrócić obiekt None

print('Zad. 1.')

import requests

agent = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

from bs4 import BeautifulSoup

def url_validator(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return "Incorrect url."
          
    url_get = requests.get(url, headers=agent)
    response_code = str(url_get.status_code)
    
    if not (response_code.startswith("2") or response_code.startswith("3")):
        return "Error response code (" + response_code + ")."
    
    soup = BeautifulSoup(url_get.text, "lxml")

    return soup

#jak przetesowałbyś tą funkcje? Co tu może pójść nie tak z tym testowaniem? Jak ją nazwałeś?

print(url_validator("htps://redeem.backtoblackvinyl.com/psy/pies.html"))
print(url_validator("https://redeem.backtoblackvinyl.com/psy/pies.html")) # 404

# Trochę nie mam pomysłu jak to testować, co może pójść nie tak? To chyba są tylko dwa ify? Czy to musi tak napierdalać całą stronę? Czy on nie może sobie gdzieś tam skrycie zwrócić tego objektu BeautifulSoup?

#To link do doskonałej inwestycji:
#https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html
#używając funkcji z poprzedniego zadania utwórz obiekt BeautifulSoup z powyższym linkiem.

# print(url_validator("https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html"))

#Napisz funkcję, która jako argument przyjmie obiekt BeautifulSoup i wyciągnie z niego cenę.

print('\n' + 'Zad. 2.')

def nedvizhimost_price_parser(soup):
    price_span = soup.find('span', {"class": "oglDetailsMoney"})
    price_output = (price_span.contents.pop(0))
    cena = int(price_output.replace(" ", ""))
    return cena

# link1 = "https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html"
# link2 = "https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-pierwotny/mieszkanie-b32-sw-piotra-87-00m2-ogl64079118.html"
# link3 = "https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/po-remoncie-gotowy-do-zamieszkania-200m2-ogrodu-ogl64109964.html"

# url_get = requests.get(link1, headers=agent)
# sup = BeautifulSoup(url_get.text, "lxml")

# print(nedvizhimost_price_parser(sup))

# url_get = requests.get(link2, headers=agent)
# sup = BeautifulSoup(url_get.text, "lxml")

# print(nedvizhimost_price_parser(sup))

# url_get = requests.get(link3, headers=agent)
# sup = BeautifulSoup(url_get.text, "lxml")

# print(nedvizhimost_price_parser(sup))

# print("\n" + "Wykorzystując url_validator z Zadania 1.:")

print(nedvizhimost_price_parser(url_validator("https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html")))
print(nedvizhimost_price_parser(url_validator("https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-pierwotny/mieszkanie-b32-sw-piotra-87-00m2-ogl64079118.html")))
print(nedvizhimost_price_parser(url_validator("https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/po-remoncie-gotowy-do-zamieszkania-200m2-ogrodu-ogl64109964.html")))

#Używaj metod z biblioteki BeautifulSoup takich jak find lub findall z odpowiednią klasą.
#W przeglądarce kliknij prawym na cenę -> zbadaj element i sprawdź jakiej klasy jest ten div/span
#Cena ma być podana jako int a nie jako string "239 000 zł"

#Znajdź 10 linków i uruchom na nich swoją metodę, czy wszystkie ceny we wszystkich linkach są pobrane bez błędów?
#Musi być 10? Nie nie musi. Dobrze by było zrobić ich wiecej jak 2