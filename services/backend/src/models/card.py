from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Boolean
from src.config.db import meta, engine

cards = Table('cards', meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('number',String(255)),
    Column('month',String(255)),
    Column('year',String(255)),
    Column('cvv',String(255)),
    Column('user_id',ForeignKey("users.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)