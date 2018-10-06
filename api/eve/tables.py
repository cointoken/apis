from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property, relationship
from sqlalchemy.dialects.mysql import (
	                                DECIMAL,BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, 
                                    DATETIME, DOUBLE, ENUM, FLOAT, INTEGER, 
                                    LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, 
                                    NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, 
                                    TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
                                    )

Base = declarative_base()


class CommonColumns(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



class Orders(CommonColumns):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    bid = Column(Integer)
    ask = Column(Integer)
    currency = Column(Integer)
    price = Column(DECIMAL(32,16))
    volume = Column(DECIMAL(32,16))
    origin_volume = Column(DECIMAL(32,16))
    state = Column(Integer)
    done_at = Column(DateTime)
    type = Column(String(8))
    member_id = Column(Integer, ForeignKey('members.id'))
    sn = Column(String(255))
    source = Column(String(255))
    ord_type = Column(String(10))
    locked = Column(DECIMAL(32,16))
    origin_locked = Column(DECIMAL(32,16))
    funds_received = Column(DECIMAL(32,16))
    trades_count = Column(Integer)
    lock_version = Column(Integer)
    average = Column(DECIMAL(32,16))
    category = Column(Integer)



class Members(CommonColumns):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    sn = Column(String(255))
    display_name = Column(String(255))
    email = Column(String(255))
    identity_id = Column(Integer)
    state = Column(Integer)
    activated = Column(Boolean)
    country_code = Column(Integer)
    phone_number = Column(String(255))
    disabled = Column(Boolean)
    api_disabled = Column(Boolean)
    nickname = Column(String(255))
    invitation_code = Column(String(255))
    password_digest = Column(String(255))
    promotion_code = Column(String(255))
    code = Column(String(255))

# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))