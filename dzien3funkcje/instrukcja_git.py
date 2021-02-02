#Obecnie wszyscy pushują commity do mastera i nikt na siebie nie patrzy, ale może to doprowadzić do konfliktów
#a tego nie chcemy
#Będziemy więc działać w następujący sposób
#Przed rozpoczęciem pracy upewniamy się, że mamy czyste repo odpalając komendę
# git status
# dostajemy info że nasz branch to master i że nie ma żadnych plików do scommitowania
# jak masz jakieś pliki to se je wyczyść albo zrób z nimi co trzeba

#Tworzymy brancha przez komendę:
#git checkout -b nazwa_brancha
#argument -b tworzy nam nowego brancha, jeżeli chcemy przejść na brancha już stworzonego to nie uzywamy tej opcji

# pracujemy i commitujemy normalnie jak trzeba na swoim lokalnym branchu

#czas wypchnąć brancha na repo po raz pierwszy:
#git push -u origin nazwa_brancha
