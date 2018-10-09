import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
# channel.queue_declare(queue='hello')
channel.exchange_declare(exchange='logs',exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs',queue=queue_name)
print('[*] Waiting for message,To exit Press Ctrl+C')


def callback(ch,method,properties,body):
	#print(ch,method,properties)
	print('[x] Received %r' % body)
	# time.sleep(15)
	# ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()
