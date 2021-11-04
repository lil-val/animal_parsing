import requests
import sys
from bs4 import BeautifulSoup
from wikipedia_table import WikipediaTable


class WikipediaPageScraper:
    """
    Representation of the wiki page
    """
    def __init__(self, url):
        self.url = url

    def scrape_table(self, position_in_page):
        """
        Getting the requested table from the requested page using BeautifulSoup
        :param position_in_page: int which represent the position of the requested table in the page
        :return: an object containing the table
        """
        page = requests.get(self.url)
        if page.status_code != 200:
            print("The requested page was not found. Please check the provided url.")
            sys.exit()
        soup = BeautifulSoup(page.content, "html.parser")
        all_tables = soup.find_all('table', {'class': 'wikitable sortable'})
        try:
            relevant_table = all_tables[position_in_page - 1].find_all('tr')
        except IndexError:
            print("The requested table was not found. Please check the provided table position.")
            sys.exit()
        return WikipediaTable(relevant_table)

