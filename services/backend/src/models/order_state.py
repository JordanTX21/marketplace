from sqlalchemy import Table, Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, String, Boolean
from src.config.db import meta, engine

# IN PREPARATION, ON WAY, DELIVERED
order_states = Table('order_states', meta, 
    Column('id',Integer,primary_key=True),
    Column('state',String(225)),
    Column('order_id',ForeignKey("orders.id"),nullable=True),
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
    Column('status',Boolean,default=True),
    )

meta.create_all(engine)