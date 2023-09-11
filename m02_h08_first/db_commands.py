import redis
from models import Author, Quote, Tag
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

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