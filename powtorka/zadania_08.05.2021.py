import os

# Jezeli chodzi o zadania na ten tydzien to by byly takie:
# 1. Napisz funkcje ktora liczy ilosc linii w pliku.
# Powinna zwracac ilosc linii pustych i z jakims tekstem.
#
# def line_count(file):
#     with open(file, 'r') as pliczek:
#         count_empty_lines = 0
#         count_written_lines = 0
#         for line in pliczek.readlines():
#             if line == '\n' or line == '':
#                 count_empty_lines += 1
#             else:
#                 count_written_lines += 1
#         return count_written_lines, count_empty_lines

# print(line_count("tekstowy.txt"))

# ni chuja kurwa nie liczy ostatniej pustej linii. DLASZEGO?!


# 2. Napisz funkcje do ktorej podasz sciezke bazowa(root directory)
# i ktora zwroci wszystkie sciezki do wszystkich plikow w tym folderze.
# Tutaj polecam google i stackoverflow.

# def list_of_files(directory):
#     file_list = []
#     directory_content = os.listdir(directory)
#     for f in directory_content:
#         file_list.append(os.path.join(directory, f))
#             # file_list.append(os.path.abspath(os.path.join(root, f)))
#     return file_list
#
# for file in list_of_files("E:\\backup\dysk_d_20200214\Chiny\z telefonu"):
#     print(file)


# import os
# print(os.path.join("E:\\backup\dysk_d_20200214\Chiny\z telefonu", "IMG_20140816_161258"))

# 3. Napisz funkcje do ktorej podasz folder bazowy, w którym są pliki tekstowe i ktora zwroci slownik
# gdzie kluczem bedzie nazwa pliku a wartoscia ilosc linii(zsumowane pelne i puste)

# def linecount_per_file(base_dir):
#     file_dict={}
#
#     directory_content = os.listdir(base_dir)
#     for f in directory_content:
#         count_of_lines = line_count(f)
#         sum_of_lines = sum(count_of_lines)
#         file_dict[f] = sum_of_lines
#     return file_dict
#
# linecount_per_file(r"C:\Users\przem\ZamenaKurs\powtorka")


# 4. Kiedys juz chyba bylo zadanie czy ja tam prezentowalem na napisanie talii kart do gry, ale mozna je powtorzyc.
# Tak wiec napisz funkcje ktora wygeneruje talie kart.
# Kazda karta niech bedzie stringiem czyli np "AS" bedzie reprezentowal asa serce ale to jak to chcesz przekazac zostawiam do wyboru.
# Moze byc dowolnie np "as|serce".
# Dalej napisz funkcje ktora przyjmie liste ze wszystkimi kartami i zwroci potasawana talie. (random)
# Dalej napisz funkcje ktora rozda karty n graczom(n jako argument do funkcji)

kolory = ['pik', 'trefl', 'karo', 'serce']
wartosci = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']

def talia_generator():
    karty = []
    for k in range(len(kolory)):
        for w in range(len(wartosci)):
            karty.append(wartosci[w],kolory[k])
    return

