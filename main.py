import datetime
import os
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv

FOUNDING_DATE = 1920


def main():
    load_dotenv()
    drinks = os.getenv("DRINKS")
    age = datetime.date.today().year - FOUNDING_DATE

    drinks_categories = pandas.read_excel(drinks)['Категория'].to_list()
    drinks_properties = pandas.read_excel(drinks, index_col='Категория') \
        .fillna('').to_dict('records')
    drinks_by_category = defaultdict(list)
    for category, property in zip(drinks_categories, drinks_properties):
        drinks_by_category[category].append(property)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        age=age,
        drinks_by_category=drinks_by_category,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
