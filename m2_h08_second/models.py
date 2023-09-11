from mongoengine import *

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(max_length=50)
    phone = StringField(max_length=50)
    subscribed = BooleanField(default=False)
    message_type = IntField(default=0)
    meta = {'collection':'contacts'}
    