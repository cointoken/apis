#-*-coding: utf-8 -*-
#Twisted Tornado Gevent Asyncio
import tornado.ioloop
import tornado.web
from tornado.httpclient import (
	                             HTTPClient,
	                             AsyncHTTPClient
	                             )
from tornado.concurrent import Future
import tornado.httpserver 

# def async_fetch_future(url):
# 	http_client = AsyncHTTPClient()
#     my_future = Future()
#     fetch_future = http_client.fetch(url)
#     fetch_future.add_done_callback(
#     	lamba f:my_future.set_result(f.result()))
#     return my_future


class WebHandler(tornado.web.RequestHandler):
	def get(self):
	    self.write({'status':'success','name':'web','code':200})


class LoginHandler(tornado.web.RequestHandler):
	def get(self):
	    self.write({'status':'success','name':'login','code':200})

	def post(self):
		try:
			username = self.get_body_argument('username')
			password = self.get_body_argument('password')
			if username and password:
				self.write({'status':'success','code':200})
		except tornado.web.MissingArgumentError as e:
			self.write({'status':'fail','code':500,'message':'提交表单字段错误'})


class AddressHandler(tornado.web.RequestHandler):
	def get(self,address_id):
	    self.write({'status':'success','address_id':address_id,'code':200})


class InfoHandler(tornado.web.RequestHandler):
	def get(self):
	    self.write({'status':'success','name':'info','code':200})


class TestHandler(tornado.web.RequestHandler):
	def get(self):
		self.write({'status':'success','name':'test','code':200})


def make_app():
	return tornado.web.Application([(r'/web',WebHandler),
		                            (r'/login',LoginHandler),
		                            (r'/address/([0-9]+)',AddressHandler),
		                            (r'/info',InfoHandler),
		                            (r'/test',TestHandler)],debug=True)


if __name__=='__main__':
	app = make_app()
	# app.listen(8080)
	http_server = tornado.httpserver.HTTPServer(app)
	# http_server.bind(8080)
	# http_server.start(2)
	http_server.listen(9090)
	tornado.ioloop.IOLoop.current().start()