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
    drinks_info = os.getenv("DRINKS_INFO")
    age = datetime.date.today().year - FOUNDING_DATE

    drinks = defaultdict(list)
    drinks_info = pandas.read_excel(drinks_info)
    drinks_info = drinks_info.fillna('')
    properties = ['Название', 'Сорт', 'Цена', 'Картинка', 'Акция']
    counter = 0
    while counter < len(drinks_info):
        current_drink = {}
        for property in properties:
            current_drink[property] = drinks_info.iloc[counter][property]

        drinks[drinks_info.iloc[counter]['Категория']].append(current_drink)
        counter += 1

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        age=age,
        drinks=drinks,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
