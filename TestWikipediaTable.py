import unittest
from wikipedia_page_scraper import WikipediaPageScraper


page = WikipediaPageScraper('https://en.wikipedia.org/wiki/List_of_animal_names')


class TestWikipediaTable(unittest.TestCase):
    def setUp(self):
        self.wikipediaTable = page.scrape_table(2)

    def test_find_relevant_columns(self):
        self.assertEqual(self.wikipediaTable.find_relevant_columns("Young", "Animal"), [1, 0])

    def test_get_relevant_columns(self):
        self.assertIn(['Aardvark', 'orycteropodian'], self.wikipediaTable.get_relevant_columns("Collateral adjective", "Animal"))


if __name__ == '__main__':
    unittest.main()
