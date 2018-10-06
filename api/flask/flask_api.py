from flask import Flask,jsonify,request
# from flask_jwt_extended import (
# 	JWTManager,jwt_required,create_access_token,
# 	jwt_refresh_token_required,create_refresh_token,
# 	get_jwt_identity
# 	)
import base64
from flask_sqlalchemy import SQLAlchemy
from exceptions import (
	                id_not_exist_exception
	)
import re

# locust
app = Flask(__name__)
# app.config['JWT_SECRET_KEY'] = 'Hex38109o'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/exchange'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
# jwt = JWTManager(app)
db = SQLAlchemy(app)
from models.orders import Orders as m_orders
from controllers.orders import Orders as c_orders


# @app.route('/login',methods=['POST'])
# def login():
# 	username = request.form.get('username',None)
# 	password = base64.b64decode(request.form.get('password',None))
	
# 	ret={'access_token':create_access_token(identity=username),'refresh_token':create_refresh_token(identity=username)}
# 	return jsonify(ret),200


# @app.route('/refresh',methods=['POST'])
# @jwt_refresh_token_required
# def refresh():
# 	current_user = get_jwt_identity()
# 	ret = {'access_token':create_access_token(identity=current_user)}
# 	return jsonify(ret),200


# @app.route('/protected',methods=['GET'])
# @jwt_required
# def protected():
# 	username = get_jwt_identity()
# 	return jsonify(logged_in_as=username),200



# @app.route('/api/v1/getaddress/<string:name>/<string:address>')
# @jwt_required
# def getaddress(name,address):
# 	if name and address:
# 		return jsonify({'status':'success','code':200,'data':{'address':address,'name':name}})



@app.route('/api/v1/get_orders_id/<int:oid>')
# @jwt_required
def get_orders_id(oid):
	o = c_orders(db)
	r = o.query_from_id(oid)
	if r is not None:
	    return jsonify({'status':'success','code':200,'data':{'bid':r.bid,'ask':r.ask}})
	else:
		raise RecordNotExistException('id not exists')


@app.errorhandler(404)
def not_found(error):
	return jsonify({'status':'fail','code':404})
# gunicorn -w 4 -b ip:8080 flask_api:app


@app.errorhandler(RecordNotExistException)
def record_not_exist(error):
	return jsonify({'status':'fail','code':500,'datas':{'error':'record not exist'}})