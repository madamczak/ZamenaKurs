#napisz funkcję która jako argument przyjmie stringa url, sprawdzi czy string rozpoczyna się od http:// lub https://
#następnie wykona request typu get, sprawdzi czy kod odpowiedzi zaczyna się na 2(OK) lub 3(Przekierowanie)
#i dalej już tylko utworzy obiekt BeautifulSoup, jako argumenty do budowy obiektu podasz tekst strony a jako parser "lxml"
#i na końcu zwróci go z funkcji
#w każdym kroku sprawdzającym możesz uznać że jeżeli warunek nie jest spełniony to możesz od razu ją przerwać i zwrócić obiekt None

#jak przetesowałbyś tą funkcje? Co tu może pójść nie tak z tym testowaniem? Jak ją nazwałeś?

#To link do doskonałej inwestycji:
#https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html
#używając funkcji z poprzedniego zadania utwórz obiekt BeautifulSoup z powyższym linkiem.

#Napisz funkcję, która jako argument przyjmie obiekt BeautifulSoup i wyciągnie z niego cenę.
#Używaj metod z biblioteki BeautifulSoup takich jak find lub findall z odpowiednią klasą.
#W przeglądarce kliknij prawym na cenę -> zbadaj element i sprawdź jakiej klasy jest ten div/span
#Cena ma być podana jako int a nie jako string "239 000 zł"

#Znajdź 10 linków i uruchom na nich swoją metodę, czy wszystkie ceny we wszystkich linkach są pobrane bez błędów?
#Musi być 10? Nie nie musi. Dobrze by było zrobić ich wiecej jak 2
