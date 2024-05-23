#!/usr/bin/env python3

from mongoengine import connect, Document, StringField, IntField, ListField, EmbeddedDocument, EmbeddedDocumentField, DateTimeField
try:
    connect(db='rptutorials', host='localhost', port=27017)
    print('Connected to MongoDB successfully')
except Exception as e:
    print(f'Error: {e}')
class User(Document):
    email = StringField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

user2 = User(email="Ondiekii0i@GMAIL.COM", first_name="Ond9iekoo", last_name="Muhindiiii")
user2.save()

user = User.objects(email="Ondiekii01@GMAIL.COM")
print(user.first_name)
user.update(first_name="Ondiek")
print(user.first_name)

#updating a record
