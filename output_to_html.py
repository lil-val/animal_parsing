class OutputToHtml:
    """
    Preparing the html file
    """
    def __init__(self, data):
        self.data = data

    def create_html_template(self, attribute_to_aggregate_by, attribute_data):
        """
        Creating html file with the aggregated data of the requested columns in a table format
        :param attribute_to_aggregate_by: str equals to the name of the column with the attribute we check for
        :param attribute_data: str equals to the name of the column with the data we want to aggregate based on the `attribute_to_aggregate_by`
        :return: html file containing the aggregated data in a table format
        """
        html = """<html>
            <head>
                <style>
                    table, th, td {
                      border: 1px solid black;
                      border-collapse: collapse;
                    }
                </style>
            </head>"""
        html += f"""
            <body>
                <table style="border:1px;">
                    <tr>
                        <th> {attribute_to_aggregate_by} </th>
                        <th> {attribute_data} </th>
                    </tr>"""
        for item in self.data:
            html += f"""<tr><td>{item}</td><td>{", ".join(self.data[item])}</td></tr>"""
        html += """</table></body></html>"""

        with open("output.html", "w", encoding='utf-8') as file:
            file.write(html)
