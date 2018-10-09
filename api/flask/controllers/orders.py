from models.orders import Orders as m_orders


class Orders():
	def __init__(self,db):
		self.db = db


	def insert(self,orders):
		if isinstance(orders,m_orders):
			self.db.add(orders)
			self.db.commit()


	def query_from_id(self,id):
		if id>0:
			return m_orders.query.filter_by(id=id).first()

	def rm(self,file):
	    import os
	    if file.delete(file)

