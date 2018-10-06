from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from tables import Orders,Members
# import os

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'apis'

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/apis'
DOMAIN = DomainConfig({
    'orders': ResourceConfig(Orders),
    'members': ResourceConfig(Members)
}).render()
