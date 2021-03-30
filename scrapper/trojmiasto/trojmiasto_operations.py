from scrapper.databases.sqlite_operations import check_if_link_exists
from scrapper.trojmiasto.website_parser import get_soup

link_template = "https://ogloszenia.trojmiasto.pl/nieruchomosci-rynek-wtorny/?strona=3"

site_number = 0

#
# while site_number < 510:
#     print(link_template + str(site_number))
#     site_number += 1

#D
def get_number_of_pages(link_template):
    number_of_pages = 0

    #check if page has advertisments
    #binary search

    return number_of_pages


#P
def parse_all_links_from_page(page_url):
    list_of_flat_dictionaries = []

    # parse all links and add them to list

    return list_of_flat_dictionaries


def get_all_links(soup):
    list_of_links= []

    all_a = soup.find_all('a', {"class": "list__item__content__title__name link"})
    for a in all_a:
        list_of_links.append(a['href'])

    return list_of_links



for link in get_all_links(get_soup(link_template)):
    print(link)




















def parse_trojmiasto():
    # check_if_link_exists
    # parse
    pass
