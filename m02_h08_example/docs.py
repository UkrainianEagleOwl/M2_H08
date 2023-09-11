import json
from models import *
from connect_mongoengine import do_connect_to_db


def load_json(filename):
    # Load data from JSON files
    with open(filename, "r") as j_file:
        json_data = json.load(j_file)
    return json_data


def insert_data_to_db(data):
    do_connect_to_db(data)
    authors_data = load_json("data/authors.json")
    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

    quotes_data = load_json("data/quotes.json")
    for quote_data in quotes_data:
        # Create Tag instances based on the "tags" data in the JSON
        tags_data = quote_data.get("tags", [])
        tags = [Tag(name=tag) for tag in tags_data]

        # Assuming you have a way to link quotes to their respective authors, you can fetch the author document here
        q = quote_data.get("quote")
        author = Author.objects(fullname=quote_data["author"]).first()
        quote = Quote(quote=q, author=author, tags=tags)
        quote.save()


if __name__ == "__main__":
    insert_data_to_db("M2_H08")
