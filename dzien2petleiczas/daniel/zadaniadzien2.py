#Zad 1 - random date
# Wygeneruj losowego integera w zakresie od 1 do 31 i przypisz go do zmiennej
# Wygeneruj losowego integera w zakresie od 1 do 12 i przypisz go do zmiennej
# Wygeneruj losowego inta w zakresie od 1970 do 2021 i przypisz go do zmiennej

print('Zad. 1a' + '\n')

import random

losowy_integer_od_1_do_31 = random.randint(1, 31)
losowy_integer_od_1_do_12 = random.randint(1, 12)
losowy_integer_od_1970_do_2021 = random.randint(1970, 2021)

print('\n')

# Używając metody format i wygenerowanych utwórz string z datą w formacie dzień-miesiąc-rok i przypisz do zmiennej

print('Zad. 1b' + '\n')

string_z_data = str(losowy_integer_od_1_do_31) + '-' + str(losowy_integer_od_1_do_12) + '-' + str(losowy_integer_od_1970_do_2021)
print(string_z_data)

print('\n')

#Utwórz z wygenerowanych wartości obiekt datetime - jakie mogą pojawić się tutaj problemy?

print('Zad. 1c' + '\n')

import datetime

zmienna_datetime = datetime.datetime.strptime(string_z_data,'%d-%m-%Y')
print(zmienna_datetime)

print('\n')

#Miesiące mają 30 albo 31 dni (oprócz lutego)
#Luty może mieć 28 lub 29 dni w zależności od roku, a generujemy inta od 1 do 31.

#Jak się przed nimi zabiezpieczyć?

#trzeba by generować zmienne począwszy od roku i zrobić ifa, albo napisać walidator, czy ten wygenerowany string string_z_data się nadaje.

print('Zad. 1d' + '\n')

import calendar

random_year = random.randint(1970, 2021)

print('Wygenerowany rok: ' + str(random_year))
print('Czy przestępny: ' + str(calendar.isleap(random_year)))

months_30d_list = [4, 6, 9, 11]
months_31d_list = [1, 3, 5, 7, 8, 10, 12]

random_month = random.randint(1, 12)
if random_month in months_30d_list:
    random_day = random.randint(1, 30)
elif random_month in months_31d_list:
    random_day = random.randint(1, 31)
elif calendar.isleap(random_year) == True:
    random_day = random.randint(1, 29)
else:
     random_day = random.randint(1, 28)

print('Wygenerowany miesiąc: ' + str(random_month))
print('Wygenerowany dzień: ' + str(random_day))

proper_random_date=(str(random_year)+str(random_month)+str(random_day))
proper_random_date=datetime.datetime.strptime(proper_random_date,'%Y%m%d')

print('W formacie datetime to by było: ' + str(proper_random_date))

print('\n')

#Zad 2 - daty i timedelta
# utwórz obiekt datetime ze swoją datą urodzenia
# jaki to był dzień? (jeżeli wiesz to super ale użyj do tego metody)
# ile dni minęło od czasu kiedy robisz to zadanie a dniem Twoich urodzin?

# utwórz obiekt datetime od kiedy (orientacyjnie) rozpocząłeś picie piwka
# zakładając że pijesz piwo tylko w piąteczek, policz ile dni byłeś w życiu pijany
# użyj do tego pętli i wzoruj się na następującym algorytmie:

# petla for
# utwórz zmienną licznik i przypisz jej wartość zero
# policz ilość dni od rozpoczęcia picia do chwili obecnej i przypisz do zmiennej ilość_dni
# dla wartości dzien z zakresu od 0 do ilość_dni
    # dodaj do daty rozpoczęcia picia tyle dni ile jest aktualnie w zmiennej dzien
    # sprawdź czy dzien który otrzymałeś to piątek
    # jeżeli to piątek to dodaj 1 do zmiennej licznik
# wyprintuj ile dni byłeś pijany

# jak zrobić to z użyciem pętli while?

# Zad 3 - Wstęp do parsowania logów txt
# w folderze dzien2petleiczas znajduje się plik logs.txt

# otwieramy go, wczytujemy wszystkie linie tekstu do zmiennej i zamykamy
log_file = open('logs.txt')
lines_from_log_file = log_file.readlines()
log_file.close()

# używając pętli znajdź linię z błędem(jest jedna taka linia) i wyprintuj ją na ekran.
# błędy w logu są raportowane w parametrze status. Wszystkie błędy mają statusy rozpoczynające się od 4
# np status=404 oznacza że strona nie istnieje
