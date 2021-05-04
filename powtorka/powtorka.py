# stringi
# startswith, endswith, indexy, znajdowanie indexów, slicing

config_file_text = """
[app_a]
whitelist.0 = server1
whitelist.1 = server[0-9]p*
whitelist.2 = server[1458][0-5]
[app_a:wtf:chujwieco]
[app_b]
whitelist.0 = server1
[app_b:trololo]
"""


# path = "C:\\aaa"
# path2 = "/aaa"
# if path.startswith("C:\\"):
#     print("windows")
# elif path.startswith("/"):
#     print("linux")
#
#
# print(config_file_text.startswith("[app_a]"))
# print(config_file_text.startswith("[app_b]"))
#
# print(config_file_text.find("[[[[app_a", 1))

def find_all(text, text_to_find):
    result = []
    current_index = 0

    while text.find(text_to_find, current_index) != -1:
        current_found = text.find(text_to_find, current_index)
        current_index = current_found + 1
        result.append(current_index - 1)

    return result


# print(find_all(config_file_text, "[app_a"))

x = "[app_a]\n"

# print(config_file_text[0 + len(x):90])

# len(x)


# print([1, 2, 3].pop(1))

x = [1, 2, 3]

# print(x)
x.extend([7, 8, 9])
# print(x)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tupla = (1, 2, 3)


dct = {"Mateusz": 33}

# print(dct.get("Mateusz"))
# print(dct.get("Przemek"))

dct["Przemek"] = 35
# print(dct.get("Mateusz"))
# print(dct.get("Przemek"))

dct.update({"Daniel": 35})

# print(dct.get("Mateusz"))
# print(dct.get("Przemek"))
# print(dct.get("Daniel"))

# print(dct.keys())
# print(dct.values())
# print(dct.items())

# for item in dct.items():
#     print(item)

# listy
# append, extend, pop
# tuple
# w tuplach tylko to co się nie zmienia

# słowniki
# klucz wartość, get, dodawanie elementu, update

# otwieranie plików i wczytywanie

# pętle for
# pętle while


# print(config_file_text)
# print(config_file_text.strip())
# print(config_file_text.strip().split("\n"))


dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
count = 0
for nucleotide in dna:
    if nucleotide.lower() == "a":
        count += 1



# print(count)
count = 0
for i in range(len(dna)):
    if dna[i].lower() == "a":
        count += 1


index = 0
max_index = len(dna)
count = 0
while index < max_index:
    nucleotide = dna[index]
    if nucleotide.lower() == "a":
        count += 1
    index += 1

print(count)
