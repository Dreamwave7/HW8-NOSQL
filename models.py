from mongoengine import connect
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField,EmbeddedDocumentField, ListField,StringField
import datetime

connect(host="mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/test?retryWrites=true&w=majority")


class Tag(EmbeddedDocument):
    name = StringField()

class Record(EmbeddedDocument):
    description = StringField()
    done = BooleanField()

class Notes(Document):
    name = StringField()
    created = DateTimeField(default=datetime.datetime.now())
    records = ListField(EmbeddedDocumentField(Record))
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {"allow_inheritance": True}









#mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/?retryWrites=true&w=majority
























