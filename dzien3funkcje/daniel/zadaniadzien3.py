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

def average2b(lst):
    if type(lst) == str:
        return "incorrect input parameter, must be list of ints"
    else:
        return sum(lst)/len(lst)

assert average2b([2,4]) == 3

print(average2b([5,8,19,21]))

# 3 napisz funkcję generującą losowe obiekty datetime. Funkcja posiada argument wejściowy ile_dni, a zwraca listę losowych obiektów datetime o takiej długości jak argument ile_dni.

print('\n'+'Zad. 3a.')

import random
from datetime import datetime, timedelta

# uwaga, funkcja generatora z netu https://gist.github.com/rg3915/db907d7455a4949dbe69

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

def random_daytime(ile_dni):
    lista_z_dniami = []
    for dzien in range(ile_dni):
        random_date = str(gen_datetime())
        lista_z_dniami.append(random_date)
    return(sorted(lista_z_dniami))

print(random_daytime(10))

# Jak sprawdzisz czy funkcja działa dobrze?
# Dodaj opcjonalny argument do funkcji który będzie decydował o tym czy zwaracana lista jest posortowana lub nie

print('\n'+'Zad. 3b.')

def random_daytime3b(ile_dni, posortowane=True):
    lista_z_dniami3b = []
    for dzien in range(ile_dni):
        random_date = str(gen_datetime())
        lista_z_dniami3b.append(random_date)
    if posortowane == True:
        lista_z_dniami3b = sorted(lista_z_dniami3b)
        return lista_z_dniami3b
    else:
        return(lista_z_dniami3b)

print(random_daytime3b(5))

# Jak sprawdzisz działanie dodatkowego argumentu?

print('\n'+'Zad. 3c.')
print("Można zrobić parę testów i sprawdzić organoleptycznie, albo z outputowanej listy zobaczyć, czy index kolejne indexy nie są niższe niż poprzednie.")

dlugosc_listy = 5
lista3c = random_daytime3b(dlugosc_listy)
print(lista3c)

for i in range(1,dlugosc_listy):
    if lista3c[i] > lista3c[i-1]:
        print(str(i) + " OK")
    else:
        print("nieposortowane")

# Pętle
# 4. Łańcuch DNA można przedstawić w postaci stringa zawierającego litery A, C, T i G
# (od nazw: Adenina, Cytozyna, Tymina i Guanina) np tak:
# 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
# a) Napisz funkcję adenine_count, która używając pętli for zwróci ile jest nukleotydów A w łańcuchu DNA

print('\n'+'Zad. 4a.')

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def adenine_count(dna):
    nukleotydy_A = 0
    for nukleotyd in range(len(dna)):
        if dna[nukleotyd] == "A":
            nukleotydy_A = nukleotydy_A + 1
    return nukleotydy_A

print(adenine_count(dna))

# b) Napisz funkcję adenine_count_while, która używając pętli while zwróci ile jest nukleotydów A w łańcuchu DNA

print('\n'+'Zad. 4b.')

def adenine_count_while(dna):
    i = 0
    nukleotydy_A = 0
    while i != len(dna):
        if dna[i] == "A":
            nukleotydy_A = nukleotydy_A + 1
        i += 1
    return nukleotydy_A

print(adenine_count_while(dna))

# c) Napisz funkcję nucleotide_count, która używając dowolnej pętli zwróci ile jest
# nukleotydów podanych w argumencie (nucleotide_type) w łańcuchu DNA
# Jak inaczej można policzyć wystąpienia nukleotydó w łańcuchu? Które podejście jest szybsze? Jak to sprawdzisz?

print('\n'+'Zad. 4c.')

def nucleotide_count(dna,nucleotide_type):
    nucleotides = ["A", "C", "T", "G"]
    if nucleotide_type not in nucleotides:
        return "Nucleotide type must be A, C, T or G"
    else:
        i = 0
        count = 0
        for i in range(len(dna)):
            if dna[i] == nucleotide_type:
                count = count + 1
        return count

print(nucleotide_count(dna,"G"))

print('\n'+'Można to zrobić jeszcze tak:')

nucletide_a_count = dna.count("A")
nucletide_c_count = dna.count("C")
nucletide_t_count = dna.count("T")
nucletide_g_count = dna.count("G")

print("There is: " + str(nucletide_a_count) + " type A nucleotides, " + str(nucletide_c_count) + " type C nucleotides, " + str(nucletide_t_count) + " type T nucleotides, and " + str(nucletide_g_count) + " type G nucleotides in provided DNA.")

# d) Napisz funkcję która jako argument przyjmie łańcuch DNA i zwróci słownik
# w którym kluczem będzie nukleotyd a wartością ilość jego wystąpień w tym łańcuchu

# e) W pliku rosalind_dna.txt masz łańcuch DNA zawierający około 900 nukleotydów. Wczytaj go i podaj zawartość
# A, T, C i G w tym łańcuchu.

# 5. Łańcuch RNA jest bardzo podobny do DNA i składa się z następujących nukleotydów A, C, U i G (U - uracyl).
# Twoim celem jest napisanie takiego samego zestawu funkcji dla RNA jak dla DNA w zadaniu 4. Jak to zrobisz?
# Będziesz kopiował? Będziesz modyfikował funkcje z zadania 4, tak żeby obsługiwały oba typy łańcuchów?
# Które podejście będzie lepsze i co z niego wyniknie?
