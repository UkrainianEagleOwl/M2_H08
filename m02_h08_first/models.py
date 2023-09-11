from mongoengine import *

class Tag(EmbeddedDocument):
    name = StringField()
    meta = {'collection':'tags'}

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()
    meta = {'collection':'authors'}
    
class Quote(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    quote = StringField(max_length=500)
    author = ReferenceField(Author)
    meta = {'collection':'quotes'}
    