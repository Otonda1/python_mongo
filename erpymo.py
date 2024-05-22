from mongoengine import connect, Document, StringField, IntField, ListField, EmbeddedDocument, EmbeddedDocumentField

connect(db='test', host='localhost', port=27017)

class City(Document):
    name = StringField(required=True, unique=True)
    population = IntField()
    country = StringField()


#nairobi = City(name='Nairobi', population=4397073, country='Kenya')
#nairobi.save()
nairobi11 = City(name='edgdggyirobii', population=43970733, country='China')

try:
    nairobi11.save()
except Exception as e:
    print(e, 'City already exists')