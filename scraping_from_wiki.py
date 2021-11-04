from wikipedia_page_scraper import WikipediaPageScraper
from output_to_html import OutputToHtml

"""
The variables below allow to retrieve data from a requested table in a wiki page.
The requested attributes (columns) can be also changed.
"""
url = 'https://en.wikipedia.org/wiki/List_of_animal_names'
position_of_table_in_page = 2
attribute_to_aggregate_by = "Collateral adjective"
attribute_data = "Animal"


def aggregate_by_primary_attribute(table):
    """
    After getting the clean table in a list format, this function aggregates the data according to the `attribute_to_aggregate_by` values
    :param table: a list containing the data of the requested columns from the wiki table
    :return: a dictionary containing the attribute_to_aggregate_by as keys and list of attribute_data as values
    """
    result = {}
    for row in table:
        for attribute_to_aggregate_by in row[1].split(','):
            attribute_to_aggregate_by.strip()
            attribute_data = row[0]
            if attribute_to_aggregate_by not in result:
                result[attribute_to_aggregate_by] = [attribute_data]
            else:
                result[attribute_to_aggregate_by] += [attribute_data]
    return result


if __name__ == '__main__':
    wikipedia_page_scraper = WikipediaPageScraper(url)
    table = wikipedia_page_scraper.scrape_table(position_of_table_in_page)
    clean_table = table.get_relevant_columns(attribute_to_aggregate_by, attribute_data)
    aggregated_data = aggregate_by_primary_attribute(clean_table)
    print(aggregated_data)
    html_output = OutputToHtml(aggregated_data)
    html_output.create_html_template(attribute_to_aggregate_by, attribute_data)

