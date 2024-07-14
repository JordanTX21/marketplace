from fastapi import APIRouter
from src.core.Recommendation import CoreRecommendation
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.config.db import SessionLocal
from src.models.voucher import vouchers
from src.models.methadata import methadata
from src.schemas.voucher import Voucher

from datetime import datetime

conn = SessionLocal()

voucher = APIRouter(
    prefix="/voucher",
    tags=["voucher"],
)


@voucher.get("/")
def index():
    result = conn.execute(vouchers.select().where(vouchers.c.status==True)).fetchall()    
    data = []
    for row in result:
        voucher_dict = dict(row._mapping)
        voucher_dict["created_at"] = voucher_dict["created_at"].isoformat()
        if voucher_dict["updated_at"]:
            voucher_dict["updated_at"] = voucher_dict["updated_at"].isoformat()
        data.append(voucher_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    return JSONResponse(content={"success": True, "message": "Lista de vouchers", "data": data})

@voucher.post("/")
def store(voucher: Voucher):
    new_voucher = {
        "type": voucher.type,
        "method_payment": voucher.method_payment,
        "amount": voucher.amount,
        "state": voucher.state,
        "created_at": datetime.now()
    }
    result = conn.execute(vouchers.insert().values(new_voucher))
    conn.commit()
    inserted_voucher_id = result.lastrowid
    
    data = conn.execute(vouchers.select().where(vouchers.c.id==inserted_voucher_id)).fetchone()
    if data is None: 
        return JSONResponse(content={"success": False, "message": "No se pudo crear el voucher"})
    product_dict = dict(data._mapping)
    product_dict["created_at"] = product_dict["created_at"].isoformat()
    if product_dict["updated_at"]:
        product_dict["updated_at"] = product_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Voucher creado", "data": product_dict}) 

@voucher.put("/{id}")
def update(id:str,voucher: Voucher):
    new_voucher = {
        "type": voucher.type,
        "method_payment": voucher.method_payment,
        "amount": voucher.amount,
        "state": voucher.state,
        "updated_at": datetime.now()
    }
    result = conn.execute(vouchers.update().values(new_voucher).where(vouchers.c.id == id))
    conn.commit()
    data = conn.execute(vouchers.select().where(vouchers.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al actualizar el voucher"})
    voucher_dict = dict(data._mapping)
    voucher_dict["created_at"] = voucher_dict["created_at"].isoformat()
    if voucher_dict["updated_at"]:
        voucher_dict["updated_at"] = voucher_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Voucher actualizado", "data": voucher_dict})

@voucher.get("/{id}")
def show(id:str):
    data =  conn.execute(vouchers.select().where(vouchers.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se encontró el voucher"})
    voucher_dict = dict(data._mapping)
    voucher_dict["created_at"] = voucher_dict["created_at"].isoformat()
    if voucher_dict["updated_at"]:
        voucher_dict["updated_at"] = voucher_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Voucher encontrado", "data": voucher_dict})

@voucher.delete("/{id}")
def delete(id:str):
    result = conn.execute(vouchers.delete().where(vouchers.c.id == id))
    conn.commit()
    if result.rowcount == 0:
        return JSONResponse(content={"success": False, "message": "No se encontró el voucher"})
    return JSONResponse(content={"success": True, "message": "Voucher eliminado"})
