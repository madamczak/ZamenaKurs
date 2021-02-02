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

#wszystkie zmiany są na branchu zdalnym na repozytorium, jeżeli zmienimy coś lokalnie to commitujemy i robimy pusha na
#ten sam branch, teraz wystarczy już git push.

#wchodzimy na stronę repozytorium - https://github.com/madamczak/ZamenaKurs/ w zakłądkę pull requests
#ustawiamy base: master, compare: nazwa_brancha i pojawia nam się diff z naszymi zmianami
#czytamy co tam zmienilismy, jeżeli coś trzeba poprawić to poprawiamy, commit i push.
#jeżeli jest ok to klikamy create pull request
#ustawiamy reviewerów - ustawiamy siebie nawzajem i klikamy create pull request

# jak zrobicie pull requesty z zadaniem domowym to się zdzwonimy i pogadamy co dalej
