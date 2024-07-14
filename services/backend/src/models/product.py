from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Float, Boolean
from src.config.db import meta, engine

products = Table('products', meta, 
    Column('id',Integer,primary_key=True),
    Column('code',String(255)),
    Column('name',String(255)),
    Column('description',Text,nullable=True),
    Column('price',Float,default=0),
    Column('min_stock',Integer,default=1),
    Column('user_id',ForeignKey("users.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)