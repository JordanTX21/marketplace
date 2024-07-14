from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import join
from src.config.db import SessionLocal
from src.models.order import orders
from src.models.order_state import order_states
from src.models.product import products
from src.models.order_detail import order_details
from datetime import datetime
from src.schemas.order import Order
from src.schemas.order_state import OrderState
from typing import Optional

conn = SessionLocal()

order = APIRouter(
    prefix="/order",
    tags=["order"],
)

@order.get("/")
def index(user_id: Optional[int] = None):
    result = conn.execute(orders.select().where(orders.c.user_id==user_id,orders.c.status==True)).fetchall()
    data = []
    for row in result:
        order_dict = dict(row._mapping)
        order_dict["created_at"] = order_dict["created_at"].isoformat()
        if order_dict["updated_at"]:
            order_dict["updated_at"] = order_dict["updated_at"].isoformat()
        result_states = conn.execute(order_states.select().where(order_states.c.order_id==order_dict["id"],order_states.c.status==True)).fetchall()
        order_dict["states"] = []
        for rstate in result_states:
            state_dict = dict(rstate._mapping)
            state_dict["created_at"] = state_dict["created_at"].isoformat()
            if state_dict["updated_at"]:
                state_dict["updated_at"] = state_dict["updated_at"].isoformat()
            order_dict["states"].append(state_dict)
        result_details = conn.execute(order_details.select().where(order_details.c.order_id==order_dict["id"],order_details.c.status==True)).fetchall()
        products_ids = [ dict(detail._mapping)["product_id"] for detail in result_details]
        result_products = conn.execute(products.select().where(products.c.status==True,products.c.id.in_(products_ids))).fetchall()
        order_dict["products"] = []
        for rproduct in result_products:
            product_dict = dict(rproduct._mapping)
            product_dict["created_at"] = product_dict["created_at"].isoformat()
            if product_dict["updated_at"]:
                product_dict["updated_at"] = product_dict["updated_at"].isoformat()
            order_dict["products"].append(product_dict)
        data.append(order_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    return JSONResponse(content={"success": True, "message": "Lista de ordenes", "data": data})
    
@order.post("/")
def store(order: Order):
    quantity = 0
    amount = 0
    for product in order.products:
        quantity += product.quantity
        amount += product.amount
    new_order = {"quantity":quantity,"amount":amount,"client_id":order.client_id,"user_id":order.user_id,"created_at": datetime.now()}
    result = conn.execute(orders.insert().values(new_order))
    result_order_states = conn.execute(order_states.insert().values({"state": "IN PREPARATION","order_id": result.lastrowid,"created_at": datetime.now()}))
    for product in order.products:
        result_order_detail = conn.execute(order_details.insert().values({"quantity": product.quantity, "amount": product.amount, "product_id": product.id,"order_id": result.lastrowid,"created_at": datetime.now()}))
    conn.commit()
    data = conn.execute(orders.select().where(orders.c.id == result.lastrowid)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al crear la orden"})
    user_dict = dict(data._mapping)
    user_dict["created_at"] = user_dict["created_at"].isoformat()
    if user_dict["updated_at"]:
        user_dict["updated_at"] = user_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Orden creada", "data": user_dict})
    
@order.put("/{id}")
def update(id:str,order: Order):
    quantity = 0
    amount = 0
    for product in order.products:
        quantity += product.quantity
        amount += product.amount
    new_order = {"quantity":quantity,"amount":amount,"client_id":order.client_id,"user_id":order.user_id,"updated_at": datetime.now()}
    result = conn.execute(orders.update().values(new_order).where(orders.c.id == id))
    conn.commit()
    data = conn.execute(orders.select().where(orders.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al actualizar la orden"})
    order_dict = dict(data._mapping)
    order_dict["created_at"] = order_dict["created_at"].isoformat()
    if order_dict["updated_at"]:
        order_dict["updated_at"] = order_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Orden actualizada", "data": order_dict})
    
@order.get("/{id}")
def show(id:str):
    data = conn.execute(orders.select().where(orders.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se encontró la orden"})
    order_dict = dict(data._mapping)
    order_dict["created_at"] = order_dict["created_at"].isoformat()
    if order_dict["updated_at"]:
        order_dict["updated_at"] = order_dict["updated_at"].isoformat()

    result_states = conn.execute(order_states.select().where(order_states.c.order_id==order_dict["id"],order_states.c.status==True)).fetchall()
    order_dict["states"] = [dict(rstate._mapping)["name"] for rstate in result_states]
    return JSONResponse(content={"success": True, "message": "Orden encontrado", "data": order_dict})
    
@order.delete("/{id}")
def destroy(id:str):
    result = conn.execute(orders.delete().where(orders.c.id == id))
    result_order_states = conn.execute(order_states.delete().where(order_states.c.order_id == id))
    conn.commit()
    return JSONResponse(content={"success": True, "message": "Orden eliminada"})

@order.post("/state/{id}")
def state(id:str,order_state:OrderState):
    result_order_states = conn.execute(order_states.insert().values({"state":order_state.state,"order_id": id,"created_at": datetime.now()}))
    conn.commit()
    return JSONResponse(content={"success": True, "message": "Estado de orden actualizado"})
    