import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!1')
print(" [x] Sent 'Hello World!'")
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!2')
print(" [x] Sent 'Hello World!'")
connection.close()
