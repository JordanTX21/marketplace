from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import InterfaceError
from src.config.db import SessionLocal
import time

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db = get_db()

def select_one(table,id: int):
    try:
        stmt = select([table]).where(clients.c.id == id)
        return db.execute(stmt).fetchone()
    except InterfaceError:
        db.rollback()
        print("Reconnecting...")
        time.sleep(1)
        return select_one(table,id)

def select_all(table,skip: int = 0, limit: int = 10):
    try:
        stmt = select([table]).offset(skip).limit(limit)
        return db.execute(stmt).fetchall()
    except InterfaceError:
        db.rollback()
        print("Reconnecting...")
        time.sleep(1)
        return select_all(table, skip, limit)

def create(table,values):
    try:
        new_client = table.insert().values(values)
        db.execute(new_client)
        db.commit()
        return new_client
    except InterfaceError:
        db.rollback()
        print("Reconnecting...")
        time.sleep(1)
        return create(table,values)

def update(table,where,values):
    try:
        stmt = table.update().where(where).values(values)
        db.execute(stmt)
        db.commit()
        return stmt
    except InterfaceError:
        db.rollback()
        print("Reconnecting...")
        time.sleep(1)
        return update(table,where,values)

def delete(table,where):
    try:
        stmt = table.delete().where(where)
        db.execute(stmt)
        db.commit()
        return stmt
    except InterfaceError:
        db.rollback()
        time.sleep(1)
        return delete(table,where)