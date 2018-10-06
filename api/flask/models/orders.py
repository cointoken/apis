try:
    from flask.flask_api import db
except:
    import sys
    sys.path.append('..')
    from flask_api import db


class Orders(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    bid = db.Column(db.Integer)
    ask = db.Column(db.Integer)
    currency = db.Column(db.Integer)
    price = db.Column(db.Float)
    volume = db.Column(db.Float)
    origin_volume = db.Column(db.Float)
    state = db.Column(db.Integer)
    done_at = db.Column(db.DateTime)
    type = db.Column(db.String(8))
    member_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    sn = db.Column(db.String(255))
    source = db.Column(db.String(255))
    ord_type = db.Column(db.String(10))
    locked = db.Column(db.Float)
    origin_locked = db.Column(db.Float)
    funds_received = db.Column(db.Float)
    trades_count = db.Column(db.Integer)
    lock_version = db.Column(db.Integer)
    average = db.Column(db.Float)
    category = db.Column(db.Integer)
