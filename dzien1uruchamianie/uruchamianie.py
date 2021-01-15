#C = 5/9 * (F - 32)

monday_temp = 38
tuesday_temp = 41
wednesday_temp = 50
thursday_temp = 32
friday_temp = 44
#ctrl + d
monday_temp_celsius = 5/9 * (monday_temp - 32)
tuesday_temp_celsius = 5/9 * (tuesday_temp - 32)
wednesday_temp_celsius = 5/9 * (wednesday_temp - 32)
thursday_temp_celsius = 5/9 * (thursday_temp - 32)
friday_temp_celsius = 5/9 * (friday_temp - 32)
#ctrl + slasz na Suwałki - komentowanie bloku kodu
# print(monday_temp_celsius)
# print(tuesday_temp_celsius)
# print(wednesday_temp_celsius)
# print(thursday_temp_celsius)
# print(friday_temp_celsius)

if thursday_temp_celsius > 5:
    print("Temp wieksza od 5" + u'\xb0' + "C")
else:
    print("Temp mniejsza od 5" + u'\xb0' "C")
