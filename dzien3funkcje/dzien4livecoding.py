

def is_prime(number):
    if type(number) != int:
        return None

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


if is_prime("DUPA"):
    print("AAAA")
else:
    print("BBBB")


def select_primes(list_of_numbers):
    list_of_primes = []

    for liczba in list_of_numbers:
        if is_prime(liczba):
            list_of_primes.append(liczba)

    return list_of_primes


def is_palindrome(word):
    reversed_word = word[::-1]
    if word.lower() == reversed_word.lower():
        return True
    else:
        return False


def select_not_palindromes(list_of_words):
    not_palindromes = []

    for word in list_of_words:
        if not is_palindrome(word):
            not_palindromes.append(word)

    return not_palindromes


kolory = ["Pik", "Trefl", "Kier", "Karo"]

figury = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

talia_kart = []

for kolor in kolory:
    for figura in figury:
        talia_kart.append(str(figura) + kolor)

import random
# print(talia_kart)
random.shuffle(talia_kart)
print(talia_kart)

gracz1 = []
gracz2 = []

for index in range(len(talia_kart)):
    if index % 2 == 0:
        gracz1.append(talia_kart.pop())
    else:
        gracz2.append(talia_kart.pop())


while len(talia_kart) > 0:
    gracz1.append(talia_kart.pop())
    gracz2.append(talia_kart.pop())


print(talia_kart)
print(gracz1)
print(gracz2)


