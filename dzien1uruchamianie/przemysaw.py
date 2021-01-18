# Zad 1. - Zmienne
# Mamy podane temperatury w stopniach F dla 7 dni tygodnia dla Boston, MA, JU ES of EJ:
# 20, 25, 30, 32, 44, 48, 40
# dla każdego z dni przelicz na stopnie C i przypisz do zmiennej.

monday_temp_b = 20
tuesday_temp_b = 25
wednesday_temp_b = 30
thursday_temp_b = 32
friday_temp_b = 44
saturday_temp_b = 48
sunday_temp_b = 40

monday_temp_f = (monday_temp_b - 32) * 5/9
tuesday_temp_f = (tuesday_temp_b - 32) * 5/9
wednesday_temp_f = (wednesday_temp_b - 32) * 5/9
thursday_temp_f = (thursday_temp_b - 32) * 5/9
friday_temp_f = (friday_temp_b - 32) * 5/9
saturday_temp_f = (saturday_temp_b - 32) * 5/9
sunday_temp_f = (sunday_temp_b - 32) * 5/9

formatted_monday = "{:.1f}".format(monday_temp_f)
formatted_tuesday = "{:.1f}".format(tuesday_temp_f)
formatted_wednesday = "{:.1f}".format(wednesday_temp_f)
formatted_thursday = "{:.1f}".format(thursday_temp_f)
formatted_friday = "{:.1f}".format(friday_temp_f)
formatted_saturday = "{:.1f}".format(saturday_temp_f)
formatted_sunday = "{:.1f}".format(sunday_temp_f)
# jak zrobic jedno miesce po przecinku, zeby sie nie jebac, tak jak ja sie jebalem

print(formatted_monday)
print(formatted_tuesday)
print(formatted_wednesday)
print(formatted_thursday)
print(formatted_friday)
print(formatted_saturday)
print(formatted_sunday)
######################################################
# Mamy podane temperatury w stopniach C dla 7 dni tygodnia - 1, 2, -2, -3, 0, 1, -1 dla Lęborka
# dla każdego z dni przelicz na stopnie F i przypisz do zmiennej.

monday_temp = -1
tuesday_temp = 2
wednesday_temp = -2
thursday_temp = -3
friday_temp = 0
saturday_temp = 1
sunday_temp = -1

monday_temp_celsius = (9/5 * monday_temp) + 32
tuesday_temp_celsius = (9/5 * tuesday_temp) + 32
wednesday_temp_celsius = (9/5 * wednesday_temp) + 32
thursday_temp_celsius = (9/5 * thursday_temp) + 32
friday_temp_celsius = (9/5 * friday_temp) + 32
saturday_temp_celsius = (9/5 * saturday_temp) + 32
sunday_temp_celsius = (9/5 * sunday_temp) + 32

print(monday_temp_celsius)
print(tuesday_temp_celsius)
print(wednesday_temp_celsius)
print(thursday_temp_celsius)
print(friday_temp_celsius)
print(saturday_temp_celsius)
print(sunday_temp_celsius)
#####################################################

# Zad 2. - Warunki
# Na pewno w poprzednim zadaniu użyłeś porządnych nazw zmiennych, w których każde słowo było od siebie oddzielone _ i
# wszystkie słowa były z małych liter? Na pewno?

# No kurwa raczej. A przynajmniej tak mnie się wydaje

# Wybierz sobie jeden z dni tygodnia z poprzedniego zadania i przeprowadź symulację rozmowy o pogodzie.
# Jeżeli w Lęborku jest zimniej niż w Bostonie wyprintuj na ekran -
# "Oooo, Panie, u nas w Lęborgu to zimno, nie to co tam w Bostonie",
# Jeżeli w Bostonie jest zimniej to wyprintuj na ekran -
# "Oooo, Panie, u nas w Lęborgu to ciepło, nie to co tam w Bostonie",

if monday_temp_celsius > monday_temp_b:
    print("Oooo, Panie, u nas w Lęborgu to ciepło, nie to co tam w Bostonie")
elif monday_temp_celsius < monday_temp_b:
    print("Oooo, Panie, u nas w Lęborgu to zimno, nie to co tam w Bostonie")
else:
    print("Oooo, Panie, u nas w Lęborgu to amerykansko pogoda je")

# Samodzielnie wymyśl co możesz powiedzieć jeżeli temperatury będą takie same.

#elif monday_temp_celsius > monday_temp_b:
#    print("Oooo, Panie, u nas w Lęborgu to amerykansko pogoda je")

# Dodatkowo możesz wyprintować jakie temperatury panują w obu tych miastach
# (tutaj może być potrzebne castowanie temperatury na typ string np. tak - str(32))

print("W Bostonie w poniedziałek było " + formatted_monday + " stopni Celsjusza, we wtorek było " + formatted_tuesday + " stopni Celsjusza, w środę " + formatted_wednesday + " stopni Celsjusza, w czwartek " + formatted_thursday + " stopni Celsjusza, w piątek " + formatted_friday + " stopni Celsjusza, w sobotę " + formatted_saturday + " stopni Celsjusza, a w niedzielę " + formatted_sunday + " stopni Celsjusza.")
print("Natomiast w Lęborgu, w poniedziałek było " + str(monday_temp) + " stopni Celsjusza, we wtorek było " + str(tuesday_temp) + " stopni Celsjusza, w środę " + str(wednesday_temp) + " stopni Celsjusza, w czwartek " + str(thursday_temp) + " stopni Celsjusza, w piątek " + str(friday_temp) + " stopni Celsjusza, w sobotę " + str(saturday_temp) + " stopni Celsjusza, a w niedzielę " + str(sunday_temp) + " stopni Celsjusza.")

###########################

# Zad 3. - Obliczenia
# Jaka jest średnia temperatura w Lęborku z zadania 1.

avg_leborg = (-1 + 2 + -2 + -3 + 0 + 1 + -1)/7
formatted_leborg = "{:.1f}".format(avg_leborg)
print("Średnia temperatura w Lęborgu to " + formatted_leborg + " stopni Celsjusza")

###################################################

# Zad 4. - Listy
# Mamy listę temperatur dla Bostonu - [20, 25, 30, 32, 44, 48, 40]
# Python ma wbudowane funkcje do różnych operacji na listach. Znajdź w google i wykonaj następujące operacje:
# suma wszystkich temperatur
# maksymalna wartość temperatury
# minimalna wartość temperatury
# Posortuj listę rosnąco
# Posortuj listę malejąco
# Dodaj do listy wartość 666
# znajdź index elementu o wartości 44
# sprawdź co robi metoda pop
# sprawdź co robi metoda append


boston = [20, 25, 30, 32, 44, 48, 40]
print(sum(boston))
print(max(boston))
print(min(boston))
boston.sort()
print(boston)
boston.sort(reverse=True)
print(boston)
boston.append(666)
print(boston)
print(boston.index(44))

########################################
# Zad 5 - Stringi
# Mamy fragment loga:
#log_fragment = "2020-12-30T16:32:40 at=info method=POST path="/gettherapistjsondetails/" status=200 bytes=9575 protocol=https"
# popraw powyższą linię w taki sposób żeby python mógł przypisać ją do zmiennej
log_fragment = '2020-12-30T16:32:40 at=info method=POST path="/gettherapistjsondetails/" status=200 bytes=9575 protocol=https'
# wywołaj metodę split() na log_fragment - nie wiesz jak? poszukaj w necie
split_func = log_fragment.split(" ")
print(split_func)
# otrzymasz listę elementów z tego stringa oddzielonych spacjami
# przypisz do zmiennej date_and_time odpowiedni element
# przypisz do zmiennej response_status odpowiedni element

# Do metody split możesz podać dowolny znak lub fragment testu którym chcesz podzielić stringa -
# utwórz zmienne date, time i status i przypisz im odpowiednie wartości