import sqlite3

from scrapper.trojmiasto.website_parser import linck2dick


# def create_db_if_not_exists(database_file_name):
#     con = sqlite3.connect(database_file_name)
#     cur = con.cursor()
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS real_estate
#                    (price int, address text, square_meter_price real, building_year int, area real, floor int,
#                     building_type text, heating_type text, number_of_rooms int, building_floors int, link text)''')
#
#     con.close()

# P
def check_if_link_exists(database_file_name, lnk):
    con = sqlite3.connect(database_file_name)
    cur = con.cursor()
    cmd = f"SELECT COUNT(*) FROM real_estate WHERE link='{lnk}'"
    cur.execute(cmd)
    all_values = cur.fetchall()
    v = all_values[0][0]
    # for v in all_values:
    #     num_of_occur = int(str(v).replace("(","").replace(",)",""))
    con.close()
    return bool(v)


    # for a in num_of_occur:
    #     if a >= 1:
    #         return "we have this in the db already"


    # if int(str(all_values).removeprefix("(").removesuffix(",)") > 1:
    #     return "Ad is in the DB already"

check_if_link_exists("example.db", 'https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html')

# D
# def insert_record(database_file_name, flat_dictionary):
#     con = sqlite3.connect(database_file_name)
#     cur = con.cursor()
#
#     cmd = f"INSERT INTO real_estate VALUES ({flat_dictionary.get('price')}, '{flat_dictionary.get('address')}, '{flat_dictionary.get('square_meter_price')}, '{flat_dictionary.get('building_year')}, '{flat_dictionary.get('area')}, '{flat_dictionary.get('floor')}, '{flat_dictionary.get('building_type')}, '{flat_dictionary.get('heating_type')}, '{flat_dictionary.get('number_of_rooms')}, '{flat_dictionary.get('building_floors')}, '{flat_dictionary.get('link')}')"
#
#
#
#     cur.execute(cmd)
#
#     con.close()

# create_db_if_not_exists('example.db')

dct = linck2dick("https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/mieszkanie-2-pokoje-gdynia-doskonala-inwestycja-ogl64070755.html")
#
# insert_record("example.db", dct)


# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','SELL','RHAT',111,35.14)")
# cur.execute("INSERT INTO stocks VALUES ('2006-01-01','SELL','RHAT',222,35.14)")
#
# con.commit()
#
# cur.execute("SELECT * FROM stocks WHERE trans='SELL'")
# all_values = cur.fetchall()
# for v in all_values:
#     print(v)
# #
#
# con.close()