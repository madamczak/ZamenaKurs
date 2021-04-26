#zadania:

# Liczenie + Daty

#1. napisz funkcję konwertującą temp w F na C, która przyjmuje listę temperatur i zwaraca listę
# # ze skonwetowanymi wartościami
#
# def fahrentheit_to_c(temp_in_f, precision=2):
#     if type(temp_in_f) == str:
#         print("Źle, popraw argument")
#
#     else:
#         return round(5 / 9 * (temp_in_f - 32), precision)
#
# # Jak sprawdzisz czy ta funkcja działa dobrze?
# # o tak:
# assert fahrentheit_to_c(32, precision=2) == 0
# assert fahrentheit_to_c(212, precision=2) == 100
#
# #2. napisz funkcję która policzy średnią arytmetyczną wartości z listy podanej jako argument do funkcji
#
# def artmtc_avg(numbers):
#     return float(sum(numbers)) / max(len(numbers), 1)
#
# lista_sredniej=[1,2,3,4,5]
#
# print(artmtc_avg(lista_sredniej))
#
# # Jakie tu mogą być problemy? Jak sprawdzisz czy funkcja działa dobrze?
#
# # ja tam nigdy nie widzę problemów niestety, a sprawdzę o tak:
# assert artmtc_avg([1,2,3,4,5]) == 3

#3. napisz funkcję generującą losowe obiekty datetime. Funkcja posiada argument wejściowy ile_dni, a zwraca listę losowych
#obiektów datetime o takiej długości jak argument ile_dni.

# import random
# import datetime
#
# random_integer_1 = random.randint(1, 31)
# random_integer_2 = random.randint(1, 12)
# random_integer_3 = random.randint(1970, 2021)
#
# date_from_random = str(random_integer_1) + '-' + str(random_integer_2) + '-' + str(random_integer_3)
#
# obiekt_datetime = datetime.datetime.strptime(date_from_random, '%d-%m-%Y')
# print(obiekt_datetime)
#
# def random_datetime(ile_dni):
#     random_datetime_list=[]
#     while ile_dni > 0:
#         ile_dni = ile_dni - 1
#         random_datetime_list.pop(obiekt_datetime)


# Jak sprawdzisz czy funkcja działa dobrze?
# Dodaj opcjonalny argument do funkcji który będzie decydował o tym czy zwaracan lista jest posortowana lub nie
# Jak sprawdzisz działanie dodatkowego argumentu?

# Pętle
# 4. Łańcuch DNA można przedstawić w postaci stringa zawierającego litery A, C, T i G
# (od nazw: Adenina, Cytozyna, Tymina i Guanina) np tak:
# 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# a) Napisz funkcję adenine_count, która używając pętli for zwróci ile jest nukleotydów A w łańcuchu DNA

# def adenine_count(dna):
#     nukleotydy_a = 0
#     for nukleotyd in range(len(dna)):
#         if dna[nukleotyd] == "A":
#             nukleotydy_a = nukleotydy_a + 1
#     return nukleotydy_a
#
# print(adenine_count(dna))
#
# # b) Napisz funkcję adenine_count_while, która używając pętli while zwróci ile jest nukleotydów A w łańcuchu DNA
#
# def adenine_count_while(dna):
#     i = 0
#     nukleotydy_A = 0
#     while i != len(dna):
#         if dna[i] == "A":
#             nukleotydy_A = nukleotydy_A + 1
#         i += 1
#     return nukleotydy_A
#
# print(adenine_count_while(dna))

# c) Napisz funkcję nucleotide_count, która używając dowolnej pętli zwróci ile jest
# nukleotydów podanych w argumencie (nucleotide_type) w łańcuchu DNA

# def nucleotide_count(dna):
#     nukleotydy_a = 0
#     nukleotydy_c = 0
#     nukleotydy_t = 0
#     nukleotydy_g = 0
#     for nukleotyd in range(len(dna)):
#         if dna[nukleotyd] == "A":
#             nukleotydy_a = nukleotydy_a + 1
#         elif dna[nukleotyd] == "C":
#             nukleotydy_c = nukleotydy_c + 1
#         elif dna[nukleotyd] == "T":
#             nukleotydy_t = nukleotydy_t + 1
#         elif dna[nukleotyd] == "G":
#             nukleotydy_g = nukleotydy_g + 1
#     return nukleotydy_a, nukleotydy_c, nukleotydy_t, nukleotydy_g
#
# print(nucleotide_count(dna))


# Jak inaczej można policzyć wystąpienia nukleotydó w łańcuchu? Które podejście jest szybsze? Jak to sprawdzisz?
# d) Napisz funkcję która jako argument przyjmie łańcuch DNA i zwróci słownik
# w którym kluczem będzie nukleotyd a wartością ilość jego wystąpień w tym łańcuchu

def nucleotide_count_dict(dna):
    count = 0
    for nukleotyd in range(len(dna)):
        if isinstance(d[x], list):
            count += len(d[x])

# e) W pliku rosalind_dna.txt masz łańcuch DNA zawierający około 900 nukleotydów. Wczytaj go i podaj zawartość
# A, T, C i G w tym łańcuchu.

# 5. Łańcuch RNA jest bardzo podobny do DNA i składa się z następujących nukleotydów A, C, U i G (U - uracyl).
# Twoim celem jest napisanie takiego samego zestawu funkcji dla RNA jak dla DNA w zadaniu 4. Jak to zrobisz?
# Będziesz kopiował? Będziesz modyfikował funkcje z zadania 4, tak żeby obsługiwały oba typy łańcuchów?
# Które podejście będzie lepsze i co z niego wyniknie?