from scrapper.databases.sqlite_operations import create_db_if_not_exists
from scrapper.trojmiasto.trojmiasto_operations import parse_trojmiasto

# config
PAGES = {"trojmiasto.pl": parse_trojmiasto}  # website name: parsing method
DATABASES = {"trojmiasto.pl": "trojmiasto_database.db"}  # website name: database file path/connection
DATABASE_CREATORS = {"trojmiasto.pl": create_db_if_not_exists}  # website name: database type specific creation method


def run(pages_to_scrap):
    # run parsing
    pass


def check_and_create_databases(pages_to_scrap):
    # check if database exists
    # create database if needed
    pass


if __name__ == "__main__":
    import argparse

    my_parser = argparse.ArgumentParser(description='')
    my_parser.add_argument('--site', type=str, help='')
    args = my_parser.parse_args()

    if args.site:
        pages_to_scrap = (args.site)
    else:
        pages_to_scrap = tuple(PAGES.keys())

    check_and_create_databases(pages_to_scrap)
    run(pages_to_scrap)
