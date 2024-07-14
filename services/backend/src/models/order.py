from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Float, Boolean
from src.config.db import meta, engine

orders = Table('orders', meta, 
    Column('id',Integer,primary_key=True),
    Column('quantity',Integer),
    Column('amount',Float),
    Column('client_id',ForeignKey("clients.id"),nullable=True),
    Column('user_id',ForeignKey("users.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)