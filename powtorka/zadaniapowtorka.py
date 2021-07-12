#Zad 1. utwórz plik z kodem dna o długości 100000 nukleotydów
#prawdopodobienstwo wystąpienia każdego z nukleotydów wynosi 25%
#podpowiedź - random.random() zwraca losową wartość float od 0 do 1
# from random import random

# def dna_generator():
#     random_float = random()
#     if random_float < 0.25:
#         print("A")
#     elif 0.25 <= random_float < 0.5:
#         print("C")
#     elif 0.5 <= random_float < 0.75:
#         print("T")
#     elif 0.75 <= random_float:
#         print("G")
#
# # zamiast print - return
#
# print(dna_generator())

# from random import choice
#
# def dna_generator(length):
#     DNA = ""
#     for count in range(length):
#         DNA += choice("CGTA")
#     return DNA
#
# text_2_add = dna_generator(100000)
#
# f = open("DNA.txt", 'w')
# f.write(str(text_2_add))
# f.close()

#Zad 2. W pliku cardata.log masz logi ze scrappera którego ostatnio pokazywałem
#Mają taką strukturę:
#LinksCollector - INFO: _getNewLinksFromCategorySite
#Nazwa modułu - poziom logowania: nazwa funkcj

#Policz ile linii logu pochodzi z modułu LinksCollector a ile z urlops (skrót od url operations,
# Paulina już dawno tą nazwe obśmiała;d "urlops, jakie kurwa urlops"
#podpowiedź - otwierasz plik i czytasz linia po linii i liczysz

# with open("cardata2.log", 'r') as file:
#     count_lc = 0
#     count_urlops = 0
#     for line in file:
#         if line.startswith("LinksCollector"):
#             count_lc += 1
#         elif line.startswith(("urlops")):
#             count_urlops += 1
#
# print(count_lc)
# print(count_urlops)


# Zad 3. Utwórz nowy plik z logiem gdzie słowo urlops zamienisz na URL Operations żeby już nikt sie z tego nie śmiał;d
# podpowiedź - otwierasz plik z logiem i czytasz wszystkie linie, tworzysz nowy plik z logiem i wpisujesz każdą linie
# ze zmnienionym urlops
# obie rzeczy robi sie podobnie ale musisz w dokumentacji metody open poczytać jaki tam trzeba dać argument żeby czytać
# a jaki żeby wpisywać lub dodawać linie do istniejącego pliku
#
with open("cardata2_final_ostateczna.log", 'w') as outfile, open("cardata2.log", 'r') as file:
    for line in file:
        if line.startswith("urlops"):
            line = line.replace("urlops", "URL Operations")
        outfile.write(line)