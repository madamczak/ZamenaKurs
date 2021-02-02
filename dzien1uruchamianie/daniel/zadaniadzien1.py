# Zad 1. - Zmienne
# Mamy podane temperatury w stopniach F dla 7 dni tygodnia dla Boston, MA, JU ES of EJ:
# 20, 25, 30, 32, 44, 48, 40
# dla każdego z dni przelicz na stopnie C i przypisz do zmiennej.

# C = 5/9 * (F - 32)

boston_monday_temp_f = 20
boston_tuesday_temp_f = 25
boston_wednesday_temp_f = 30
boston_thursday_temp_f = 32
boston_friday_temp_f = 44
boston_saturday_temp_f = 48
boston_sunday_temp_f = 40

boston_monday_temp_c = round(5 / 9 * (boston_monday_temp_f - 32), 0)
boston_tuesday_temp_c = round(5 / 9 * (boston_tuesday_temp_f - 32), 0)
boston_wednesday_temp_c = round(5 / 9 * (boston_wednesday_temp_f - 32), 0)
boston_thursday_temp_c = round(5 / 9 * (boston_thursday_temp_f - 32), 0)
boston_friday_temp_c = round(5 / 9 * (boston_friday_temp_f - 32), 0)
boston_saturday_temp_c = round(5 / 9 * (boston_saturday_temp_f - 32), 0)
boston_sunday_temp_c = round(5 / 9 * (boston_sunday_temp_f - 32), 0)

print('Zad. 1a' + '\n')

print(boston_monday_temp_c, u'\xb0C')
print(boston_tuesday_temp_c, u'\xb0''C')
print(boston_wednesday_temp_c, u'\xb0C')
print(boston_thursday_temp_c, u'\xb0C')
print(boston_friday_temp_c, u'\xb0C')
print(boston_saturday_temp_c, u'\xb0C')
print(boston_sunday_temp_c, u'\xb0C')

# Mamy podane temperatury w stopniach C dla 7 dni tygodnia - 1, 2, -2, -3, 0, 1, -1 dla Lęborka
# dla każdego z dni przelicz na stopnie F i przypisz do zmiennej.

lebork_monday_temp_c = 1
lebork_tuesday_temp_c = 2
lebork_wednesday_temp_c = -2
lebork_thursday_temp_c = -3
lebork_friday_temp_c = 0
lebork_saturday_temp_c = 1
lebork_sunday_temp_c = -1

# T(°F) = T(°C) × 9/5 + 32

lebork_monday_temp_f = round(lebork_monday_temp_c * 9 / 5 + 32, 2)
lebork_tuesday_temp_f = round(lebork_tuesday_temp_c * 9 / 5 + 32, 2)
lebork_wednesday_temp_f = round(lebork_wednesday_temp_c * 9 / 5 + 32, 2)
lebork_thursday_temp_f = round(lebork_thursday_temp_c * 9 / 5 + 32, 2)
lebork_friday_temp_f = round(lebork_friday_temp_c * 9 / 5 + 32, 2)
lebork_saturday_temp_f = round(lebork_saturday_temp_c * 9 / 5 + 32, 2)
lebork_sunday_temp_f = round(lebork_sunday_temp_c * 9 / 5 + 32, 2)

print('\n')

print('Zad. 1b' + '\n')

print(lebork_monday_temp_f, u'\xb0F')
print(lebork_tuesday_temp_f, u'\xb0F')
print(lebork_wednesday_temp_f, u'\xb0F')
print(lebork_thursday_temp_f, u'\xb0F')
print(lebork_friday_temp_f, u'\xb0F')
print(lebork_saturday_temp_f, u'\xb0F')
print(lebork_sunday_temp_f, u'\xb0F')

print('\n')

# Zad 2. - Warunki
# Na pewno w poprzednim zadaniu użyłeś porządnych nazw zmiennych, w których każde słowo było od siebie oddzielone _ i
# wszystkie słowa były z małych liter? Na pewno?

# Wybierz sobie jeden z dni tygodnia z poprzedniego zadania i przeprowadź symulację rozmowy o pogodzie.
# Jeżeli w Lęborku jest zimniej niż w Bostonie wyprintuj na ekran -
# "Oooo, Panie, u nas w Lęborgu to zimno, nie to co tam w Bostonie",
# Jeżeli w Bostonie jest zimniej to wyprintuj na ekran -
# "Oooo, Panie, u nas w Lęborgu to ciepło, nie to co tam w Bostonie",

# Samodzielnie wymyśl co możesz powiedzieć jeżeli temperatury będą takie same.

print('Zad. 2a' + '\n')

if lebork_friday_temp_c < boston_thursday_temp_c:
    print("Oooo, Panie, u nas w Lęborgu to zimno, nie to co tam w Bostonie")
elif lebork_friday_temp_c > boston_thursday_temp_c:
    print("Oooo, Panie, u nas w Lęborgu to ciepło, nie to co tam w Bostonie")
else:
    print(
        "Oooo, Panie, u nas w Lęborgu to zimno, ale to wszędy tak: mam wuja w Bostonie, i on mówi, że tam jest to samo, uciec donikąd, a kostucha blisko.")

print('\n')

# Dodatkowo możesz wyprintować jakie temperatury panują w obu tych miastach
# (tutaj może być potrzebne castowanie temperatury na typ string np. tak - str(32))

print('Zad. 2b' + '\n')

print('W Lęborku w poniedziałek ' + str(lebork_monday_temp_c) + u'\xb0C' + ', a w Bostonie ' + str(
    boston_monday_temp_c) + u'\xb0C')
print('W Lęborku we wtorek ' + str(lebork_tuesday_temp_c) + u'\xb0C' + ', a w Bostonie ' + str(
    boston_tuesday_temp_c) + u'\xb0C')
print('W Lęborku w środę ' + str(lebork_wednesday_temp_c) + u'\xb0C' + ', a w Bostonie ' + str(
    boston_wednesday_temp_c) + u'\xb0C')
print('W Lęborku w czwartek ' + str(lebork_thursday_temp_c) + u'\xb0C' + ', a w Bostonie ' + str(
    boston_thursday_temp_c) + u'\xb0C')
print('W Lęborku w piątek ' + str(lebork_friday_temp_c) + u'\xb0C' + ', a w Bostonie ' + str(
    boston_friday_temp_c) + u'\xb0C')
print('W Lęborku w sobotę ' + str(lebork_saturday_temp_c) + u'\xb0C' + ', a w Bostonie ' + str(
    boston_saturday_temp_c) + u'\xb0C')
print('W Lęborku w niedzielę ' + str(lebork_sunday_temp_c) + u'\xb0C' + ', a w Bostonie ' + str(
    boston_sunday_temp_c) + u'\xb0C')

print('\n')

# Zad 3. - Obliczenia
# Jaka jest średnia temperatura w Lęborku z zadania 1.

print('Zad. 3' + '\n')

average_temp_c_lebork_poland = (
                                           lebork_monday_temp_c + lebork_tuesday_temp_c + lebork_wednesday_temp_c + lebork_thursday_temp_c + lebork_friday_temp_c + lebork_saturday_temp_c + lebork_sunday_temp_c) / 7

print(
    'Average temperature in Lębork, Poland for the week is: ' + str(round(average_temp_c_lebork_poland, 2)) + u'\xb0C')
print('\n')

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

print('Zad. 4' + '\n')

boston_temp_f_list = [20, 25, 30, 32, 44, 48, 40]

print('suma wszystkich temperatur: ' + str(sum(boston_temp_f_list)))
print('maksymalna wartość temperatury: ' + str(max(boston_temp_f_list)))
print('minimalna wartość temperatury: ' + str(min(boston_temp_f_list)))
print('lista posortowana rosnąco: ' + str(sorted(boston_temp_f_list, reverse=False)))
print('lista posortowana malejąco: ' + str(sorted(boston_temp_f_list, reverse=True)))

szatan = [666]

print('dodana wartość 666 (\\m/): ' + str(boston_temp_f_list + szatan))
print('index elementu o wartości 44: ' + str(boston_temp_f_list.index(44)))
print('metoda pop robi tak: ' + str(boston_temp_f_list.pop(0)))
print('metoda append robi tak: ' + str(boston_temp_f_list.append('append')))
print('ta lista po tym wszystkim co jej uczyniłem: ' + str(boston_temp_f_list))

print('\n')

# Zad 5 - Stringi
# Mamy fragment loga:

print('Zad. 5a' + '\n')

log_fragment = '2020-12-30T16:32:40 at=info method=POST path="/gettherapistjsondetails/" status=200 bytes=9575 protocol=https'

# popraw powyższą linię w taki sposób żeby python mógł przypisać ją do zmiennej
# wywołaj metodę split() na log_fragment - nie wiesz jak? poszukaj w necie
# otrzymasz listę elementów z tego stringa oddzielonych spacjami
# przypisz do zmiennej date_and_time odpowiedni element
# przypisz do zmiennej response_status odpowiedni element

splitted_log_fragment = log_fragment.split()
print(splitted_log_fragment)
date_and_time = splitted_log_fragment.pop(0)
print(date_and_time)
response_status = splitted_log_fragment.pop(3)
print(response_status)

print('\n')

# Do metody split możesz podać dowolny znak lub fragment testu którym chcesz podzielić stringa -
# utwórz zmienne date, time i status i przypisz im odpowiednie wartości


print('Zad. 5b' + '\n')

splitted_date_and_time = date_and_time.split(sep='T')
splitted_response_status = response_status.split(sep='=')

date = splitted_date_and_time.pop(0)
time = splitted_date_and_time.pop(0)
status = splitted_response_status.pop(1)

print(date)
print(time)
print(status)

# Bandziorno, senkju
