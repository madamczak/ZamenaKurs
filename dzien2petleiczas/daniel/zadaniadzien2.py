#Zad 1 - random date
# Wygeneruj losowego integera w zakresie od 1 do 31 i przypisz go do zmiennej
# Wygeneruj losowego integera w zakresie od 1 do 12 i przypisz go do zmiennej
# Wygeneruj losowego inta w zakresie od 1970 do 2021 i przypisz go do zmiennej

print('Zad. 1a')

import random

losowy_integer_od_1_do_31 = random.randint(1, 31)
losowy_integer_od_1_do_12 = random.randint(1, 12)
losowy_integer_od_1970_do_2021 = random.randint(1970, 2021)

print('Nie ma tu nic ciekawego do wyprintowania')

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

## Miesiące mają 30 albo 31 dni (oprócz lutego)
## Luty może mieć 28 lub 29 dni w zależności od roku, a generujemy inta od 1 do 31.

#Jak się przed nimi zabiezpieczyć?

## trzeba by generować zmienne począwszy od roku i zrobić ifa, albo napisać walidator, czy ten wygenerowany string string_z_data się nadaje.

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

print('Zad. 2a' + '\n')

birthday = datetime.datetime.strptime('1986-10-10','%Y-%m-%d')
print(birthday)

# jaki to był dzień? (jeżeli wiesz to super ale użyj do tego metody)

week_days_pl = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

birthday_weekday=datetime.datetime.weekday(birthday)

print('Born on ' + str(week_days_pl.pop(birthday_weekday)))

# ile dni minęło od czasu kiedy robisz to zadanie a dniem Twoich urodzin?

## print(datetime.datetime.now())
## Wyszło 2021-01-25 00:31:03.596597

homework_now = datetime.datetime.strptime('2021-01-25 00:31:03.596597','%Y-%m-%d %H:%M:%S.%f')

homework_since_birthday = homework_now-birthday
print('homework_since_birthday: ' + str(homework_since_birthday))

print('\n')

print('Zad. 2b' + '\n')

# utwórz obiekt datetime od kiedy (orientacyjnie) rozpocząłeś picie piwka

## to musiał być jakoś styczeń 2004 roku, więc załóżmy, że to była połowa stycznia, a dokładnie 2004-01-15.

wszystko_sie_zaczelo = datetime.datetime.strptime('2004-01-15','%Y-%m-%d')

# zakładając że pijesz piwo tylko w piąteczek, policz ile dni byłeś w życiu pijany
# użyj do tego pętli i wzoruj się na następującym algorytmie:
# petla for
# utwórz zmienną licznik i przypisz jej wartość zero

licznik = 0

# policz ilość dni od rozpoczęcia picia do chwili obecnej i przypisz do zmiennej ilość_dni

ilosc_dni = (datetime.datetime.now()-wszystko_sie_zaczelo).days

# dla wartości dzien z zakresu od 0 do ilość_dni
    # dodaj do daty rozpoczęcia picia tyle dni ile jest aktualnie w zmiennej dzien
    # sprawdź czy dzien który otrzymałeś to piątek
    # jeżeli to piątek to dodaj 1 do zmiennej licznik
# wyprintuj ile dni byłeś pijany

for dzien in range(0, ilosc_dni):
    wszystko_sie_zaczelo = wszystko_sie_zaczelo + datetime.timedelta(days = 1)
    if datetime.datetime.weekday(wszystko_sie_zaczelo) == 4:
        licznik = licznik + 1
print('Nazywam się Daniel Sikora i metodologią pętli for obliczyłem, że byłem pijany ' + str(licznik) + ' dni.')

## wynik jest ok, ale coś mi tu nie pasuje, próbowałem dodawać zmienną dzien w ten sposób:
##    wszystko_sie_zaczelo = wszystko_sie_zaczelo + datetime.timedelta(days = dzien)
## ale wtedy dodawało mi cztery lata za każdym razem (nie rozumiem dlaczego) i w końcu wyjebuje, że OverflowError: date value out of range

# jak zrobić to z użyciem pętli while?

time_flies = datetime.datetime.strptime('2004-01-15','%Y-%m-%d')
counter = 0

while time_flies < datetime.datetime.now():
    time_flies += datetime.timedelta(days = 1)
    if datetime.datetime.weekday(time_flies) == 4:
        counter = counter + 1
print('Nazywam się Daniel Sikora i metodologią pętli while obliczyłem, że byłem pijany ' + str(counter) + ' dni.')

print('\n')

# Zad 3 - Wstęp do parsowania logów txt
# w folderze dzien2petleiczas znajduje się plik logs.txt

# otwieramy go, wczytujemy wszystkie linie tekstu do zmiennej i zamykamy

print('Zad. 3' + '\n')

import os
parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

log_file = open(os.path.join(parentDirectory, 'ZamenaKurs\\dzien2petleiczas' ,'logs.txt'))
lines_from_log_file = log_file.readlines()
log_file.close()

# używając pętli znajdź linię z błędem(jest jedna taka linia) i wyprintuj ją na ekran.
# błędy w logu są raportowane w parametrze status. Wszystkie błędy mają statusy rozpoczynające się od 4
# np status=404 oznacza że strona nie istnieje

line = 1
for line in lines_from_log_file:
    if line.find('status=4')>= 0:
        print(line)