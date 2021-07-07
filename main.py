import json
from pprint import pprint
import wikipediaapi


class WikiIter:

    def __init__(self, items):
        self.items = iter(items)

    def __iter__(self, ):
        return self

    def __next__(self, ):
        name = next(self.items)
        wiki_wik = wikipediaapi.Wikipedia('en')
        page = wiki_wik.page(name).fullurl
        return page


with open("countries.json") as f:
    countries_file = json.load(f)

country_list = []     # Создаем список стран из исходного файла

for country in countries_file:
    name_country = country['name']['common']
    country_list.append(name_country)
# pprint(country_list)

link_list = []      # Находим ссылки через итератор

for link in WikiIter(country_list):
    link_list.append(link)
# pprint(url_list)

new_file = dict(zip(country_list, link_list))  # Создаем словарь для записи файла

with open("new_file.json", "w") as f:   # Записываем новый файл в формате .json
    json.dump(new_file, f)
