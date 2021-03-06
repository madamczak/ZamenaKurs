# formatowanie stringów
# print("formatowanie stringów:")
temp_boston = 2
typ1plusy = "W Lęborgu jest teraz " + str(0) + " stopni Celsjusza, a w Bostonie " + str(temp_boston)
# trzeba pamiętać o typach danych i castować

typ2procenty = "W Lęborgu jest teraz %d stopni Celsjusza, a w Bostonie %s" % (0, str(temp_boston))
# dalej trzeba pamiętać o typach danych %d - inty, %s - stringi, %f - floaty
# trzeba pamiętać o kolejności po %
#
typ3format = "W Lęborgu jest teraz {} stopni Celsjusza, a w Bostonie {}".format(0, temp_boston)
# nie trzeba pamiętać o typie danych ale kolejność i ilość {} jest ważna
#
typ4fstringi = f"W Lęborgu jest teraz {0} stopni Celsjusza, a w Bostonie {temp_boston}"
# Chyba najłatwiejsze podejście ale działa tylko w Pythonie 3.
#
# print(typ1plusy)
# print(typ2procenty)
# print(typ3format)
# print(typ4fstringi)


# listy vs tuple
# print("\nlisty vs tuple")
# lista = [1, 2, 3]
# tupla = ("1", 2, 3)
# print(lista, tupla)
# lista[0] = 666
# # tupla[0] = 666 to nie zadziała bo nie można modyfikować tupli
# print(lista, tupla)
#
# listy vs sety
# print("\nlisty vs sety")
# lista = []
# zbior = set()
# print(lista, zbior)
# lista.append(1)
# lista.append(2)
# lista.append(3)
#
# zbior.add(1)
# zbior.add(2)
# zbior.add(3)
# #
# print(lista, zbior)
# lista.append(3)
# zbior.add(3)
# print(lista, zbior)
#
# lista.append(lista)
# print("Lista z dodaną do siebie listą:", lista)
# print("Lista z listy", lista[-1])
#zbior.add(zbior) # - to nie zadziała bo Bertrand Russell
# print("Zbior z dodanym do siebie zbiorem", zbior)

# nie używaj w pętli for listy którą będziesz modyfikował w tej właśnie pętli
# lst = [1, 2, 3]
# for i in lst:
#     lst.append(i)
#     print(lst)


# 2 sposoby na otwieranie i zamykanie plików

# fl = open(file_path, "a")
# # kod
# fl.close()

# with open(file_path, mode) as fl:

# kod

# wczytywanie i parsowaniem .txt
# wczytywanie i parsowaniem .csv
# wczytywanie i parsowanie XMLi - później
# wczytywanie i parsowanie JSONów


# for line in csv_file.readlines():
#     #print("LINE:", line)
#     stripped_line = line.strip()
#     # print("STRIPPED LINE:", stripped_line)
#     splt_line = stripped_line.split("  ")
#     print(splt_line)

import csv
# csv_file = open("dane/biostats.csv")
# print("CSV")
# # csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
# # for row in csv_reader:
# #     print(row)
# #
# csv_dct_reader = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)
# people = []
# #
# for row in csv_dct_reader:
#     weight_lbs = row.get('Weight (lbs)')
#     #1lb = 0.45359237 kg
#     row['Weight (kg)'] = int(weight_lbs) * 0.45359237
#     people.append(row)
#     # print(row)
# # print(people)
# # for element in people:
# #     print(element)
# #
# csv_file.close()


# new_csv_file = open('dane/new_csv.csv', "w")
# writer = csv.DictWriter(new_csv_file, fieldnames=people[0].keys())
# writer.writeheader()
# for person in people:
#     writer.writerow(person)
# new_csv_file.close()

import json
# json_file = open("dane/biostats.json")
# loaded = json.load(json_file)
# print(loaded)
# #
# new_json_file = open("dane/new_json.json", "w")
# json.dump(people, new_json_file)



# funkcje

def fahrentheit_to_c(temp_in_f, precision=2):
    if type(temp_in_f) == str:
        print("Źle, popraw argument")

    else:
        return round(5 / 9 * (temp_in_f - 32), precision)

assert fahrentheit_to_c(32, precision=5) == 0
assert fahrentheit_to_c(212, precision=5) == 100

# testowanie funkcji
