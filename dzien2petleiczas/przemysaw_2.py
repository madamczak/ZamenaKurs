#Zad 1 - random date
# Wygeneruj losowego integera w zakresie od 1 do 31 i przypisz go do zmiennej
import random
random_integer_1 = random.randint(1, 31)
print(random_integer_1)
# Wygeneruj losowego integera w zakresie od 1 do 12 i przypisz go do zmiennej
random_integer_2 = random.randint(1, 12)
print(random_integer_2)
# Wygeneruj losowego inta w zakresie od 1970 do 2021 i przypisz go do zmiennej
random_integer_3 = random.randint(1970, 2021)
print(random_integer_3)
# Używając metody format i wygenerowanych utwórz string z datą w formacie dzień-miesiąc-rok i przypisz do zmiennej
date_from_random = str(random_integer_1) + '-' + str(random_integer_2) + '-' + str(random_integer_3)
print(date_from_random)
# zacząłem kombinować z formatem, ale poległem
#print("{:-<2}".format(random_integer_1),"{:-<2}".format(random_integer_2))


#Utwórz z wygenerowanych wartości obiekt datetime - jakie mogą pojawić się tutaj problemy?
import datetime
obiekt_datetime = datetime.datetime.strptime(date_from_random, '%d-%m-%Y')
print(obiekt_datetime)

#Jak się przed nimi zabiezpieczyć?
#miesiąsce mają po 30 i 31 dni, Luty jest pojebany - jakaś walidacja po wygenerowaniu daty

#Zad 2 - daty i timedelta
# utwórz obiekt datetime ze swoją datą urodzenia
datetime_urodziny = datetime.datetime.strptime('1986-11-17', '%Y-%m-%d')
# jaki to był dzień? (jeżeli wiesz to super ale użyj do tego metody)
dzien_urodzin = datetime.datetime.weekday(datetime_urodziny)
print(str(dzien_urodzin) + ' czyli poniedzialek')
# ile dni minęło od czasu kiedy robisz to zadanie a dniem Twoich urodzin?
print(datetime.datetime.now())
#2021-01-30 21:29:39.898123

czas_teraz = datetime.datetime.strptime('2021-01-30', '%Y-%m-%d')
roznica_dni = czas_teraz - datetime_urodziny
print(roznica_dni)

# utwórz obiekt datetime od kiedy (orientacyjnie) rozpocząłeś picie piwka
piwko_start = (datetime.datetime.strptime('2004-02-01', '%Y-%m-%d'))
# zakładając że pijesz piwo tylko w piąteczek, policz ile dni byłeś w życiu pijany
# użyj do tego pętli i wzoruj się na następującym algorytmie:

# petla for
import calendar
# utwórz zmienną licznik i przypisz jej wartość zero
licznik = 0
# policz ilość dni od rozpoczęcia picia do chwili obecnej i przypisz do zmiennej ilość_dni
czas_picia = (czas_teraz - piwko_start).days
print(czas_picia)
# dla wartości dzien z zakresu od 0 do ilość_dni
    # dodaj do daty rozpoczęcia picia tyle dni ile jest aktualnie w zmiennej dzien
    # sprawdź czy dzien który otrzymałeś to piątek
    # jeżeli to piątek to dodaj 1 do zmiennej licznik


for dzien in range (0, czas_picia):
    piwko_start = piwko_start + datetime.timedelta(days=1)
    if datetime.datetime.weekday(piwko_start)  == 4:
        licznik = licznik + 1

# wyprintuj ile dni byłeś pijany
print('cześć, jestem przemek, w swoim zyciu byłem pijany ' + str(licznik) + ' dni')
# jak zrobić to z użyciem pętli while?
licznik_while = 0
while piwko_start < czas_teraz:
    piwko_start += datetime.timedelta(days = 1)
    if datetime.datetime.weekday(piwko_start) == 4:
        licznik_while = licznik_while + 1
print('cześć, jestem przemek, w swoim zyciu byłem pijany ' + str(licznik_while) + ' dni')
# Zad 3 - Wstęp do parsowania logów txt
# w folderze dzien2petleiczas znajduje się plik logs.txt

# otwieramy go, wczytujemy wszystkie linie tekstu do zmiennej i zamykamy
log_file = open('logs.txt')
lines_from_log_file = log_file.readlines()
log_file.close()

# używając pętli znajdź linię z błędem(jest jedna taka linia) i wyprintuj ją na ekran.
# błędy w logu są raportowane w parametrze status. Wszystkie błędy mają statusy rozpoczynające się od 4
# np status=404 oznacza że strona nie istnieje
