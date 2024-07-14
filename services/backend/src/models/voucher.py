from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Float, String, Boolean
from src.config.db import meta, engine

vouchers = Table('vouchers', meta, 
    Column('id',Integer,primary_key=True),
    Column('type',String(225), default='BV'),
    Column('method_payment',String(225)),
    Column('amount',Float, default=0),
    Column('state',String(225), default='CA'),
    Column('order_id',ForeignKey("orders.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)