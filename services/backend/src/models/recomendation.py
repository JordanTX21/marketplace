from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Float, Boolean
from src.config.db import meta, engine

recomendations = Table('recomendations', meta, 
    Column('id',Integer,primary_key=True),
    Column('product_id',ForeignKey("products.id"),nullable=True),
    Column('user_id',ForeignKey("users.id"),nullable=True),
    Column('order',Integer),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)