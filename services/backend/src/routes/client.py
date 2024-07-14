from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.config.db import SessionLocal
from src.models.client import clients
from datetime import datetime
from src.schemas.client import Client
from typing import Optional


conn = SessionLocal()

client = APIRouter(
    prefix="/client",
    tags=["client"],
)

@client.get("/")
def index(user_id: Optional[int] = None):
    query = clients.select().where(clients.c.status==True,clients.c.user_id==user_id)
    # if user_id is not None:
    result = conn.execute(query).fetchall()
    data = []
    for row in result:
        client_dict = dict(row._mapping)
        client_dict["created_at"] = client_dict["created_at"].isoformat()
        if client_dict["updated_at"]:
            client_dict["updated_at"] = client_dict["updated_at"].isoformat()
        data.append(client_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    return JSONResponse(content={"success": True, "message": "Lista de clientes","user_id":user_id, "data": data})

@client.post("/")
def store(client : Client):
    new_client = {
        "type_document": client.type_document,
        "document": client.document,
        "name": client.name,
        "address": client.address,
        "email": client.email,
        "user_id": client.user_id,
        "created_at": datetime.now()
    }
    result = conn.execute(clients.insert().values(new_client))
    conn.commit()
    inserted_client_id = result.lastrowid
    data = conn.execute(clients.select().where(clients.c.id==inserted_client_id)).fetchone()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se pudo crear el cliente"})
    
    client_dict = dict(data._mapping)
    client_dict["created_at"] = client_dict["created_at"].isoformat()
    if client_dict["updated_at"]:
        client_dict["updated_at"] = client_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Cliente creado", "data": client_dict})

@client.put("/{id}")
def update(id:str, client: Client):
    new_client = {
        "type_document": client.type_document,
        "document": client.document,
        "name": client.name,
        "address": client.address,
        "email": client.email,
        "user_id": client.user_id,
        "updated_at": datetime.now()
    }
    result = conn.execute(clients.update().values(new_client).where(clients.c.id == id))
    conn.commit()
    data = conn.execute(clients.select().where(clients.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al actualizar el cliente"})
    client_dict = dict(data._mapping)
    client_dict["created_at"] = client_dict["created_at"].isoformat()
    if client_dict["updated_at"]:
        client_dict["updated_at"] = client_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Cliente actualizado", "data": client_dict})

@client.get("/{id}")
def show(id:str):
    data = conn.execute(clients.select().where(clients.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se encontró al cliente"})
    client_dict = dict(data._mapping)
    client_dict["created_at"] = client_dict["created_at"].isoformat()
    if client_dict["updated_at"]:
        client_dict["updated_at"] = client_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Cliente encontrado", "data": client_dict})


@client.delete("/{id}")
def delete(id:str):
    result = conn.execute(clients.delete().where(clients.c.id == id))
    conn.commit()
    return JSONResponse(content={"success": True, "message": "Cliente eliminado"})

