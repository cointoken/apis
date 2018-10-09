#-*-coding: utf-8 -*-
import pika 

connection = pika.BlockingConnection(
	pika.ConnectionParameters('localhost',5672))

channel = connection.channel() 
# channel.queue_declare(queue='hello') #队列
channel.exchange_declare(exchange='logs',exchange_type='fanout')#,   #广播管道
	                     #type='fanout')
# for i in range(10):
channel.basic_publish(exchange='logs',
	                  routing_key='',
	                  body='Hello World')

print('[x] Sent hello world!')
connection.close()
