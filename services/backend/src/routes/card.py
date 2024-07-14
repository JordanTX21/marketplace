from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.config.db import SessionLocal
from src.models.card import cards
from datetime import datetime
from src.schemas.card import Card
from typing import Optional


conn = SessionLocal()

card = APIRouter(
    prefix="/card",
    tags=["card"],
)

@card.get("/")
def index(user_id: Optional[int] = None):
    query = cards.select().where(cards.c.status==True,cards.c.user_id==user_id)
    # if user_id is not None:
    result = conn.execute(query).fetchall()
    data = []
    for row in result:
        card_dict = dict(row._mapping)
        card_dict["created_at"] = card_dict["created_at"].isoformat()
        if card_dict["updated_at"]:
            card_dict["updated_at"] = card_dict["updated_at"].isoformat()
        data.append(card_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    return JSONResponse(content={"success": True, "message": "Lista de tarjetas","user_id":user_id, "data": data})

@card.post("/")
def store(card : Card):
    new_card = {
        "name": card.name,
        "number": card.number,
        "month": card.month,
        "year": card.year,
        "cvv": card.cvv,
        "user_id": card.user_id,
        "created_at": datetime.now()
    }
    result = conn.execute(cards.insert().values(new_card))
    conn.commit()
    inserted_card_id = result.lastrowid
    data = conn.execute(cards.select().where(cards.c.id==inserted_card_id)).fetchone()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se pudo crear la tarjeta"})

    card_dict = dict(data._mapping)
    card_dict["created_at"] = card_dict["created_at"].isoformat()
    if card_dict["updated_at"]:
        card_dict["updated_at"] = card_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Tarjeta creada", "data": card_dict})

@card.put("/{id}")
def update(id:str, card: Card):
    new_card = {
        "name": card.name,
        "number": card.number,
        "month": card.month,
        "year": card.year,
        "cvv": card.cvv,
        "user_id": card.user_id,
        "created_at": datetime.now()
    }
    result = conn.execute(cards.update().values(new_card).where(cards.c.id == id))
    conn.commit()
    data = conn.execute(cards.select().where(cards.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al actualizar la tarjeta"})
    card_dict = dict(data._mapping)
    card_dict["created_at"] = card_dict["created_at"].isoformat()
    if card_dict["updated_at"]:
        card_dict["updated_at"] = card_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Tarjeta actualizada", "data": card_dict})

@card.get("/{id}")
def show(id:str):
    data = conn.execute(cards.select().where(cards.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se encontró la tarjeta"})
    card_dict = dict(data._mapping)
    card_dict["created_at"] = card_dict["created_at"].isoformat()
    if card_dict["updated_at"]:
        card_dict["updated_at"] = card_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Tarjeta encontrado", "data": card_dict})


@card.delete("/{id}")
def delete(id:str):
    result = conn.execute(cards.delete().where(cards.c.id == id))
    conn.commit()
    return JSONResponse(content={"success": True, "message": "Tarjeta eliminada"})

