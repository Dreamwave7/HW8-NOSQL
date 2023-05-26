import pika
from faker import *
from mongoengine import *
from models_users import Contacts
import os
from random import randint
import json

fake = Faker()
url = os.environ.get('CLOUDAMQP_URL', 'amqps://aorwbbgt:wHGa_268pn_QbEPfX2bUESraKvnjGglG@hawk.rmq.cloudamqp.com/aorwbbgt')
params = pika.URLParameters(url)
connectn = pika.BlockingConnection(params)
channel = connectn.channel()

channel.exchange_declare(exchange="task", exchange_type="direct")
channel.queue_declare(queue="message", durable=True)
channel.queue_bind(exchange="task", queue="message")

def seed():
    for i in range(10):
        user = Contacts(
            fullname = fake.name(),
            email = fake.email(),
            age = randint(20,30),
            send_sms = False
            ).save()
        

def main():
    contact_list = Contacts.objects()
    for i in contact_list:
        message = {
            "id": str(i["id"]),
            "task": f"call to {fake.name()}"
            }
    
        
        channel.basic_publish(
            exchange="task",
            routing_key="message",
            body= json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
            )
    
    connectn.close()

if __name__ == "__main__":
    seed()
    main()
        















































































