from models import *
import pprint
import json

dict_authors = {}


def seed_authors():
    with open("authors.json") as file:
        authors = json.load(file)

    for i in authors:
        author = Authors(
            fullname = i["fullname"],
            born_date = i["born_date"],
            born_location = i["born_location"],
            description = i["description"]
            )
        dict_authors[i["fullname"]] = author
        author.save()

def seed_quotes():
    with open("quotes.json", encoding="utf8") as file:
        quotes = json.load(file)
    for i in quotes:
        author = i["author"]
        quote = Quotes(
            tags = i["tags"],
            author = dict_authors[author],
            quote = i["quote"]
            )
        quote.save()

seed_authors()
seed_quotes()



