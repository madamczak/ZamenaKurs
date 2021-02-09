#zadania:

# Liczenie + Daty

# 1. napisz funkcję konwertującą temp w F na C, która przyjmuje listę temperatur i zwaraca listę ze skonwetowanymi wartościami

print('Zad. 1')

def f_to_c(temp_f, precision=2):
    return round(5 / 9 * (temp_f - 32), precision)

# Jak sprawdzisz czy ta funkcja działa dobrze?

## assertem

assert f_to_c(32, precision=5) == 0
assert f_to_c(212, precision=5) == 100

print(f_to_c(32))

print('\n'+'Zad. 2a.')

# 2. napisz funkcję która policzy średnią arytmetyczną wartości z listy podanej jako argument do funkcji

def average(lista):
    return sum(lista)/len(lista)

print(average([10,20,10,20]))

# Jakie tu mogą być problemy? Jak sprawdzisz czy funkcja działa dobrze?

## problemy? może być niepoprawny format wejścia
## można sprawdzić też assertem

print('\n'+'Zad. 2b.')

def average(lst):
    if type(lst) == str:
        return print("incorrect input parameter, must be list of ints")
    else:
        return sum(lst)/len(lst)

assert average([2,4]) == 3

print(average([5,8,19,21]))

# 3 napisz funkcję generującą losowe obiekty datetime. Funkcja posiada argument wejściowy ile_dni, a zwraca listę losowych obiektów datetime o takiej długości jak argument ile_dni.

print('\n'+'Zad. 3a.')

import random

def random_day(ile_dni):
    lista_z_dniami = []
    for dzien in ile_dni:
        append.lista_z_dniami(random.date_and_time)

print(random_day(3))
print(lista_z_dniami)

# Jak sprawdzisz czy funkcja działa dobrze?
# Dodaj opcjonalny argument do funkcji który będzie decydował o tym czy zwaracan lista jest posortowana lub nie
# Jak sprawdzisz działanie dodatkowego argumentu?

# Pętle
# 4. Łańcuch DNA można przedstawić w postaci stringa zawierającego litery A, C, T i G
# (od nazw: Adenina, Cytozyna, Tymina i Guanina) np tak:
# 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
# a) Napisz funkcję adenine_count, która używając pętli for zwróci ile jest nukleotydów A w łańcuchu DNA
# b) Napisz funkcję adenine_count_while, która używając pętli while zwróci ile jest nukleotydów A w łańcuchu DNA
# c) Napisz funkcję nucleotide_count, która używając dowolnej pętli zwróci ile jest
# nukleotydów podanych w argumencie (nucleotide_type) w łańcuchu DNA
# Jak inaczej można policzyć wystąpienia nukleotydó w łańcuchu? Które podejście jest szybsze? Jak to sprawdzisz?
# d) Napisz funkcję która jako argument przyjmie łańcuch DNA i zwróci słownik
# w którym kluczem będzie nukleotyd a wartością ilość jego wystąpień w tym łańcuchu

# e) W pliku rosalind_dna.txt masz łańcuch DNA zawierający około 900 nukleotydów. Wczytaj go i podaj zawartość
# A, T, C i G w tym łańcuchu.

# 5. Łańcuch RNA jest bardzo podobny do DNA i składa się z następujących nukleotydów A, C, U i G (U - uracyl).
# Twoim celem jest napisanie takiego samego zestawu funkcji dla RNA jak dla DNA w zadaniu 4. Jak to zrobisz?
# Będziesz kopiował? Będziesz modyfikował funkcje z zadania 4, tak żeby obsługiwały oba typy łańcuchów?
# Które podejście będzie lepsze i co z niego wyniknie?
