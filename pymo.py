#!/usr/bin/env python3
from mongoengine import connect, Document, StringField, IntField

# Connect to the MongoDB database
try:
    connect(db="rptutorials", host="localhost", port=27017)
    print("Connected to MongoDB successfully")
except Exception as e:
    print(f"Error: {e}")

# Define a User document
class User(Document):
    name = StringField(required=True)
    age = IntField(required=True)

# Create and save a new user
user = User(name="John Doe", age=30)
user.save()
user2 = User(name="Jane Doe", age=25)
user2.save()

# Retrieve all users
users = User.objects()
for user in users:
    print(user.name, user.age)

# Retrieve a specific user
john = User.objects(name="John Doe").first()
print(john.name, john.age)
