import pika

def main():
    credent = pika.PlainCredentials("aorwbbgt","wHGa_268pn_QbEPfX2bUESraKvnjGglG")
    connect = pika.BlockingConnection(pika.ConnectionParameters(host="hawk-01.rmq.cloudamqp.com",port=1883,credentials=credent))

    channel = connect.channel()

    channel.queue_declare(queue="Test")

    channel.basic_publish(exchange="", routing_key="Test",body="Hello i try send message to rabbitmq".encode())
    connect.close()


if __name__ == '__main__':
    main()



