from mongoengine import *

connect(db='test', host='localhost', port=27017)

class Student(EmbeddedDocument):
    name = StringField()
    registration = StringField()

class Teacher(Document):
    name = StringField()
    age = IntField()
    students = ListField(EmbeddedDocumentField(Student))

teacher = Teacher(
    name="Mr. John",
    age=40,
    students=[
        Student(name="Jane Doe", registration="2020-001"),
        Student(name="John Doe", registration="2020-002")
    ])
teacher.save()

teacher = Teacher.objects(name="Mr. John").first()
print(teacher.students[0].name)