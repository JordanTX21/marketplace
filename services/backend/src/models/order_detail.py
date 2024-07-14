from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Float, Boolean
from src.config.db import meta, engine

order_details = Table('order_details', meta, 
    Column('id',Integer,primary_key=True),
    Column('quantity',Integer),
    Column('amount',Float),
    Column('product_id',ForeignKey("products.id"),nullable=True),
    Column('order_id',ForeignKey("orders.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)