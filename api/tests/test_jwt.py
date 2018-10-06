# -*- coding:utf-8 -*-
import base64
import unittest
from warnings import warn
from exceptions import InvalidError
import logging
import time
import datetime
import threading


class _config():
	@property
	def my_key(self):
		raise InvalidError('ccc')
		# warn()
		# return 'ccc'
'''
payload
iss 签发者
sub 面向的用户
aud 接收jwt的另一方
exp jwt过期时间
nbf 定义在什么时间之前
iat 签发时间
jti 唯一身份标识
'''
def create_token(userid):
	header = byte({'alg':'HS256','typ':'JWT'})


def test_encode_header():
	header =  byte({'alg':'HS256','typ':'JWT'})
	print(base64.urlsafe_b64encode(header))


def test_decode_header():
	print(base64.urlsafe_b64decode(b'eydhbGcnOidIUzI1NicsJ3R5cGUnOidKV1QnfQ=='))


class Redis(object):
	def __init__(self,host='localhost',port=6379,db=0):
		self.host = host
		self.port = port
		self.db = db
   


if __name__=='__main__':
    # test_decode_header()
    # c = _config()
    # FORMAT = '%(asctime)-15s %(clientip)s'
    # logging.basicConfig(format=FORMAT)
    # ip = {'clientip':'192.168.1.109'}
    # logging.warning('no exit',extra=ip)
    # print(c.my_key)
    redis = Redis(host='127.0.0.1')
    print(redis.host,redis.port)
    
