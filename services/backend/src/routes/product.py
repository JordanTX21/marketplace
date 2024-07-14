from fastapi import APIRouter
from src.core.Recommendation import CoreRecommendation
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.config.db import SessionLocal
from src.models.product import products
from src.models.product_image import product_images
from src.models.product_rate import product_rates
from src.models.product_category import product_categories
from src.models.methadata import methadata
from src.models.user import users
from src.models.recomendation import recomendations
from datetime import datetime
from src.schemas.product import Product
from src.schemas.product_search import ProductSearch
from sqlalchemy import select
import requests
import re
import unicodedata
import random
import string

conn = SessionLocal()

product = APIRouter(
    prefix="/product",
    tags=["product"],
)

@product.get("/recomended")
def recomended():
    id=22
    result = conn.execute(methadata.select().where(methadata.c.user_id==id and methadata.c.status==True)).fetchall()
    methadatas = [dict(data._mapping)["type"] for data in result]
    # text_search = 'I need Men casual t-shits'
    text_search = 'I need '+' '.join(methadatas)
    items = get_recommend_items(text_search, top_k=5)
    i=0
    for item in items:
        i+=1
        result = conn.execute(recomendations.insert().values({"user_id":id,"product_id":int(item["id"][4:]),"order":i,"created_at":datetime.now()}))
    conn.commit()
    return JSONResponse(content={"success": True, "message": "Lista de productos", "data": jsonable_encoder(items)})

@product.get("/recomendations/{user_id}")
def get_recomendations(user_id:int):
    result_rec = conn.execute(recomendations.select().where(recomendations.c.user_id==user_id,recomendations.c.status==True)).fetchall()
    products_ids = [dict(data._mapping)["product_id"] for data in result_rec]
    result = conn.execute(products.select().where(products.c.id.in_(products_ids),products.c.status==True)).fetchall()
    data = []
    for row in result:
        product_dict = dict(row._mapping)
        product_dict["created_at"] = product_dict["created_at"].isoformat()
        if product_dict["updated_at"]:
            product_dict["updated_at"] = product_dict["updated_at"].isoformat()
        images = conn.execute(product_images.select().where(product_images.c.product_id==product_dict["id"] and product_images.c.status==True)).fetchall()
        product_dict["images"] = [dict(img._mapping)["image"] for img in images]
        product_dict["image"] = product_dict["images"][0]
        rate = conn.execute(product_rates.select().where(product_rates.c.product_id==product_dict["id"] and product_rates.c.status==True)).first()
        rate = dict(rate._mapping) if rate is not None else None
        product_dict["rating"] = {
            "rate": rate["rate"] if rate is not None else 0,
            "count": rate["count"] if rate is not None else 0
        }
        categories = conn.execute(product_categories.select().where(product_categories.c.product_id==product_dict["id"] and product_categories.c.status==True)).fetchall()
        categories = [dict(category._mapping)["name"] for category in categories]
        product_dict["categories"] = categories
        product_dict["category"] = categories[0]
        data.append(product_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    return JSONResponse(content={"success":True,"message":"Lista de productos","data":data})

@product.get("/")
def index():
    result = conn.execute(products.select().where(products.c.status==True)).fetchall()
    data = []
    for row in result:
        product_dict = dict(row._mapping)
        product_dict["created_at"] = product_dict["created_at"].isoformat()
        if product_dict["updated_at"]:
            product_dict["updated_at"] = product_dict["updated_at"].isoformat()
        images = conn.execute(product_images.select().where(product_images.c.product_id==product_dict["id"] and product_images.c.status==True)).fetchall()
        product_dict["images"] = [dict(img._mapping)["image"] for img in images]
        product_dict["image"] = product_dict["images"][0]
        rate = conn.execute(product_rates.select().where(product_rates.c.product_id==product_dict["id"] and product_rates.c.status==True)).first()
        rate = dict(rate._mapping) if rate is not None else None
        product_dict["rating"] = {
            "rate": rate["rate"] if rate is not None else 0,
            "count": rate["count"] if rate is not None else 0
        }
        categories = conn.execute(product_categories.select().where(product_categories.c.product_id==product_dict["id"] and product_categories.c.status==True)).fetchall()
        categories = [dict(category._mapping)["name"] for category in categories]
        product_dict["categories"] = categories
        product_dict["category"] = categories[0]
        data.append(product_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    return JSONResponse(content={"success":True,"message":"Lista de productos","data":data})

@product.post("/")
def store(product: Product):
    new_product = {
        "name":product.name,
        "code":f"{create_slug(product.name)}-{string_random(10)}",
        "description":product.description,
        "price":product.price,
        "min_stock":product.min_stock,
        "user_id":product.user_id,
        "created_at": datetime.now()
    }
    result = conn.execute(products.insert().values(new_product))
    conn.commit()
    inserted_product_id = result.lastrowid
    if product.images:
        for image_path in product.images:
            conn.execute(product_images.insert().values({
                "image": image_path,
                "product_id": inserted_product_id,
                "created_at": datetime.now(),
            }))
    if product.categories:
        for category in product.categories:
            conn.execute(product_categories.insert().values({
                "name": category,
                "product_id": inserted_product_id,
                "created_at": datetime.now(),
            }))
    data = conn.execute(products.select().where(products.c.id == inserted_product_id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al crear el producto"})
    product_dict = dict(data._mapping)
    product_dict["created_at"] = product_dict["created_at"].isoformat()
    if product_dict["updated_at"]:
        product_dict["updated_at"] = product_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Producto creado", "data": product_dict})

@product.put("/{id}")
def update(id:str,product: Product):
    new_product = {
        "name":product.name,
        "description":product.description,
        "price":product.price,
        "min_stock":product.min_stock,
        "user_id":product.user_id,
        "updated_at": datetime.now()
    }
    # Actualizar las imágenes si se proporcionan nuevas imágenes
    conn.execute(product_images.delete().where(product_images.c.product_id == id))
    conn.execute(product_categories.delete().where(product_categories.c.product_id == id))
    result = conn.execute(products.update().values(new_product).where(products.c.id == id))
    if product.images:
        # Guardar las rutas de las nuevas imágenes en la tabla product_images
        for image_path in product.images:
            conn.execute(product_images.insert().values({
                "image_path": image_path,
                "product_id": id,
                "created_at": datetime.now(),
            }))
    if product.categories:
        for category in product.categories:
            conn.execute(product_categories.insert().values({
                "name": category,
                "product_id": id,
                "created_at": datetime.now(),
            }))
    conn.commit()
    data = conn.execute(products.select().where(products.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al crear el producto"})
    product_dict = dict(data._mapping)
    product_dict["created_at"] = product_dict["created_at"].isoformat()
    if product_dict["updated_at"]:
        product_dict["updated_at"] = product_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Producto creado", "data": product_dict})

@product.get("/{code}")
def show(code:str):
    data = conn.execute(products.select().where(products.c.code == code)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se encontró el producto"})
    product_dict = dict(data._mapping)
    product_dict["created_at"] = product_dict["created_at"].isoformat()
    if product_dict["updated_at"]:
        product_dict["updated_at"] = product_dict["updated_at"].isoformat()
    if product_dict["user_id"] is not None:
        user = conn.execute(users.select().where(users.c.id == product_dict["user_id"])).first()
        product_dict["user"] = dict(user._mapping)
        product_dict["user"]["created_at"] = product_dict["user"]["created_at"].isoformat()
        if product_dict["user"]["updated_at"]:
            product_dict["user"]["updated_at"] = product_dict["user"]["updated_at"].isoformat()
    images = conn.execute(product_images.select().where(product_images.c.product_id==product_dict["id"] and product_images.c.status==True)).fetchall()
    product_dict["images"] = [dict(img._mapping)["image"] for img in images]
    product_dict["image"] = product_dict["images"][0]
    rate = conn.execute(product_rates.select().where(product_rates.c.product_id==product_dict["id"] and product_rates.c.status==True)).first()
    rate = dict(rate._mapping) if rate is not None else None
    product_dict["rating"] = {
        "rate": rate["rate"] if rate is not None else 0,
        "count": rate["count"] if rate is not None else 0
    }
    categories = conn.execute(product_categories.select().where(product_categories.c.product_id==product_dict["id"] and product_categories.c.status==True)).fetchall()
    categories = [dict(category._mapping)["name"] for category in categories]
    product_dict["categories"] = categories
    product_dict["category"] = categories[0]
    return JSONResponse(content={"success": True, "message": "Producto encontrado", "data": product_dict})

@product.delete("/{id}")
def destroy(id:str):
    conn.execute(product_images.delete().where(product_images.c.product_id == id))
    conn.execute(product_categories.delete().where(product_categories.c.product_id == id))
    result = conn.execute(products.delete().where(products.c.id == id))
    conn.commit()
    return JSONResponse(content={"success": True, "message": "Producto eliminado"})

@product.post("/search")
def search(product_search:ProductSearch):
    if len(product_search.name) < 3:
        return JSONResponse(content={"success": False, "message": "Ingrese una busqueda válida"})
    where = products.select().where(products.c.status==True,products.c.name.like(f"%{product_search.name}%"))
    if product_search.min_price is not None:
        where.where(products.c.price>=product_search.min_price)
    if product_search.max_price is not None:
        where.where(products.c.price<=product_search.max_price)
    if product_search.order_by is not None:
        where.order_by(products.c[product_search.order_by].desc())
    else:
        where.order_by(products.c.created_at.desc())
    result = conn.execute(where).fetchall()
    data = []
    for row in result:
        product_dict = dict(row._mapping)
        product_dict["created_at"] = product_dict["created_at"].isoformat()
        if product_dict["updated_at"]:
            product_dict["updated_at"] = product_dict["updated_at"].isoformat()
        images = conn.execute(product_images.select().where(product_images.c.product_id==product_dict["id"] and product_images.c.status==True)).fetchall()
        product_dict["images"] = [dict(img._mapping)["image"] for img in images]
        product_dict["image"] = product_dict["images"][0]
        rate = conn.execute(product_rates.select().where(product_rates.c.product_id==product_dict["id"] and product_rates.c.status==True)).first()
        rate = dict(rate._mapping) if rate is not None else None
        product_dict["rating"] = {
            "rate": rate["rate"] if rate is not None else 0,
            "count": rate["count"] if rate is not None else 0
        }
        categories = conn.execute(product_categories.select().where(product_categories.c.product_id==product_dict["id"] and product_categories.c.status==True)).fetchall()
        categories = [dict(category._mapping)["name"] for category in categories]
        product_dict["categories"] = categories
        product_dict["category"] = categories[0]
        data.append(product_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    result_methadata = conn.execute(methadata.select().where(methadata.c.type==product_search.name,methadata.c.user_id==product_search.user_id,methadata.c.status==True)).first()
    if result_methadata is not None:
        result_methadata = dict(result_methadata._mapping)
        conn.execute(methadata.update().values({"points":result_methadata["points"]+1}).where(methadata.c.id==result_methadata["id"]))
    else:
        conn.execute(methadata.insert().values({
            "type": product_search.name,
            "points": 1,
            "user_id": product_search.user_id
        }))
    conn.commit()
    
    return JSONResponse(content={"success":True,"message":"Lista de productos","data":data})

def get_recommend_items(text, top_k=2):
    api_url = 'http://127.0.0.1:8000/api/product/'
    c_search = CoreRecommendation(api_url)
    items = c_search.recommended_products(text, top_k)
    return items

def create_slug(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Normalizar caracteres unicode
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('ascii')
    # Reemplazar espacios y caracteres no alfanuméricos
    texto = re.sub(r'[^a-z0-9]+', '-', texto)
    # Eliminar guiones al principio y al final
    texto = texto.strip('-')
    return texto

def string_random(longitud):
    caracteres = string.ascii_letters + string.digits
    cadena_aleatoria = ''.join(random.choices(caracteres, k=longitud))
    return cadena_aleatoria