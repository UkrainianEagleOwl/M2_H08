from models import Author, Quote, Tag
from connect_mongoengine import do_connect_to_db
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

def connect_to_database():
    # Replace with your MongoDB cloud connection URI and database name
    do_connect_to_db('M2_H08')


@cache
def search_by_author_name(author_name):
    author = Author.objects(fullname__istartswith =author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return quotes
    else:
        return []


@cache
def search_by_tag(tag):
    quotes = Quote.objects(tags__name=tag)
    return quotes


@cache
def search_by_tags(tag_list):
    tags = Tag.objects(name__in=tag_list)
    if tags:
        quotes = Quote.objects(tags__in=tags)
        return quotes
    else:
        return []

def main():
    connect_to_database()
    
    while True:
        user_input = input("Enter command: ").strip()
        
        if user_input.startswith("name:"):
            author_name = user_input[5:].strip()
            quotes = search_by_author_name(author_name)
        elif user_input.startswith("tag:"):
            tag = user_input[4:].strip()
            quotes = search_by_tag(tag)
        elif user_input.startswith("tags:"):
            tag_list = user_input[5:].strip().split(",")
            quotes = search_by_tags(tag_list)
        elif user_input == "exit":
            break
        else:
            print("Invalid command. Please use 'name:', 'tag:', 'tags:', or 'exit'.")
            continue

        # Print the quotes in utf-8 format
        for quote in quotes:
            print(quote.quote.encode('utf-8').decode('utf-8'))

if __name__ == "__main__":
    main()