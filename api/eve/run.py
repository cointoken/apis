from eve import Eve
import os
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from tables import Base,Orders,Members
# from eve_auth_jwt import requires_token
# from eve_auth_jwt import JWTAuth

# second_auth=JWTAuth()
# second_auth.secret = 'custom_secret'
# second_auth.issuer = 'custom_issuer'
app = Eve(validator=ValidatorSQL, data=SQL)
db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base

db.create_all()
# db.session.add_all([Parent(children=[Child() for k in range(n)])
#                     for n in range(10)])
# db.session.commit()

# using reloader will destroy the in-memory sqlite db
app.run(host='192.168.0.107',port=8080,debug=True, use_reloader=False)

