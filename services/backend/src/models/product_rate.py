from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Float, Boolean
from src.config.db import meta, engine

product_rates = Table('product_rates', meta, 
    Column('id',Integer,primary_key=True),
    Column('rate',Float,default=0),
    Column('count',Integer,default=0),
    Column('product_id',ForeignKey("products.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)