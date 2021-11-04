import re
import sys


class WikipediaTable:
    """
    Representation of the requested table from the wiki page
    """
    def __init__(self, table):
        self.table = table

    def find_relevant_columns(self, primary_attribute, attribute_to_sort):
        """
        find the relevant indexes in the table based on the columns names
        :param primary_attribute: str equals to the name of the column with the attribute we check for
        :param attribute_to_sort: str equals to the name of the column with the data we want to aggregate based on the primary attribute
        :return: list containing the indexes of the requested columns
        """
        index_of_primary_attribute = -1
        index_of_attribute_to_sort = -1
        for row in self.table:
            if index_of_primary_attribute != -1 and index_of_attribute_to_sort != -1:
                continue
            columns = row.find_all('th')
            for column in range(len(columns)):
                if columns[column].get_text() == primary_attribute:
                    index_of_primary_attribute = column
                if columns[column].get_text() == attribute_to_sort:
                    index_of_attribute_to_sort = column
        if index_of_primary_attribute == -1 or index_of_attribute_to_sort == -1:
            print("The required columns were not found in the requested table.")
            sys.exit()
        return [index_of_primary_attribute, index_of_attribute_to_sort]

    def get_relevant_columns(self, attribute_to_aggregate_by, attribute_data):
        """
        Getting the data from the requested columns.
        Clean the data by removing some html tags, links to lists and references
        :param attribute_to_aggregate_by: str equals to the name of the column with the attribute we check for
        :param attribute_data: str equals to the name of the column with the data we want to aggregate based on the primary attribute
        :return: list of lists, each nested list holds the values of the requested columns of a row in the table
        """
        index_of_primary_attribute, index_of_attribute_to_sort = self.find_relevant_columns(attribute_to_aggregate_by, attribute_data)
        required_max_index = max(index_of_primary_attribute, index_of_attribute_to_sort)
        clean_table = []
        for row in self.table:
            cells = row.find_all('td')
            if len(cells) >= required_max_index:
                for tag in cells[index_of_primary_attribute].find_all('br'):
                    tag.replace_with(',')
                for tag in cells[index_of_attribute_to_sort].find_all('br'):
                    tag.replace_with(',')
                attribute_to_aggregate_by = cells[index_of_primary_attribute].get_text().replace("(list)", "").replace("  ", " ").strip()
                attribute_data = cells[index_of_attribute_to_sort].get_text().replace("(list)", "").replace("  ", " ").strip()
                attribute_data = re.sub(r'\[.*\]', '', attribute_data)
                clean_table.append([attribute_data, attribute_to_aggregate_by])
        if len(clean_table) == 0:
            print("No relevant lines were found in the requested table")
            sys.exit()
        return clean_table

