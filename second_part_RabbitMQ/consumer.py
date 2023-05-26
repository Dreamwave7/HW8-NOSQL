import pika
import json
import os
from mongoengine import *
from models_users import *

url = os.environ.get('CLOUDAMQP_URL', 'amqps://aorwbbgt:wHGa_268pn_QbEPfX2bUESraKvnjGglG@hawk.rmq.cloudamqp.com/aorwbbgt')
params = pika.URLParameters(url)
connectn = pika.BlockingConnection(params)
channel = connectn.channel()

channel.queue_declare(queue="message",durable=True)

def callback(ch, method,properties, body):
    message = json.loads(body.decode())
    print(message, "--- message recieved")
    userid = message.get("id")
    change_flag(userid)
    ch.basic_ack(delivery_tag=method.delivery_tag)



def change_flag(iduser):
    contact = Contacts.objects(id = iduser)
    contact.update(send_sms = True)



channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="message", on_message_callback=callback)

if __name__ == "__main__":
    channel.start_consuming()