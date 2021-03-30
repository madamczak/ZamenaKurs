import sqlite3


def create_db_if_not_exists(database_file_name):
    con = sqlite3.connect(database_file_name)
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS real_estate
                   (price int, address text, square_meter_price real, building_year int, area real, floor int,
                    building_type text, heating_type text, number_of_rooms int, building_floors int, link text)''')

    con.close()


def check_if_link_exists(database_file_name, lnk):
    con = sqlite3.connect(database_file_name)
    cur = con.cursor()
    cmd = f"SELECT COUNT(*) FROM real_estate WHERE link='{lnk}'"
    cur.execute(cmd)
    all_values = cur.fetchall()
    v = all_values[0][0]
    con.close()
    return bool(v)


def insert_record(database_file_name, flat_dictionary):
    con = sqlite3.connect(database_file_name)
    cur = con.cursor()

    cmd = f"INSERT INTO real_estate VALUES (" \
          f"{flat_dictionary.get('price')}, " \
          f"'{flat_dictionary.get('address')}', " \
          f"{flat_dictionary.get('square_meter_price')}, " \
          f"{flat_dictionary.get('building_year')}, " \
          f"{flat_dictionary.get('area')}, " \
          f"{flat_dictionary.get('floor')}, " \
          f"'{flat_dictionary.get('building_type')}', " \
          f"'{flat_dictionary.get('heating_type')}', " \
          f"{flat_dictionary.get('number_of_rooms')}, " \
          f"{flat_dictionary.get('building_floors')}, " \
          f"'{flat_dictionary.get('link')}')"
    cur.execute(cmd)
    con.commit()
    con.close()
