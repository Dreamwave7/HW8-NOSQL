from mongoengine import *

connect(host="mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/module8?retryWrites=true&w=majority")

class Contacts(Document):
    fullname = StringField()
    email = StringField()
    age = IntField()
    send_sms = BooleanField()
