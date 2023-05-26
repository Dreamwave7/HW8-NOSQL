import pika
from faker import *
from mongoengine import *
from models import
import os


url = os.environ.get('CLOUDAMQP_URL', 'amqps://aorwbbgt:wHGa_268pn_QbEPfX2bUESraKvnjGglG@hawk.rmq.cloudamqp.com/aorwbbgt')
params = pika.URLParameters(url)
connectn = pika.BlockingConnection(params)
channel = connectn.channel()

channel.exchange_declare(exchange="task", exchange_type="direct")
channel.queue_declare(queue="message", durable=True)
channel.queue_bind(exchange="task", queue="message")

def seed():
    for i in range(10):
        user = Contacts




















































































