from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from src.config.db import meta, engine

clients = Table('clients', meta, 
    Column('id',Integer,primary_key=True),
    Column('type_document',String(255)),
    Column('document',String(255)),
    Column('name',String(255)),
    Column('address',String(255)),
    Column('email',String(255)),
    Column('user_id',ForeignKey("users.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)