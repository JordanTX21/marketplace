from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Text, Boolean
from src.config.db import meta, engine

product_images = Table('product_images', meta, 
    Column('id',Integer,primary_key=True),
    Column('image',Text,nullable=True),
    Column('product_id',ForeignKey("products.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)