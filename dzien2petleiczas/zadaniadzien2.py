#Zad 1 - random date
# Wygeneruj losowego integera w zakresie od 1 do 31 i przypisz go do zmiennej
# Wygeneruj losowego integera w zakresie od 1 do 12 i przypisz go do zmiennej
# Wygeneruj losowego inta w zakresie od 1970 do 2021 i przypisz go do zmiennej

# Używając metody format i wygenerowanych utwórz string z datą w formacie dzień-miesiąc-rok i przypisz do zmiennej

#Utwórz z wygenerowanych wartości obiekt datetime - jakie mogą pojawić się tutaj problemy?
#Jak się przed nimi zabiezpieczyć?

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
