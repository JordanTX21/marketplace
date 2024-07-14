from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.config.db import SessionLocal
from src.models.user import users
from src.schemas.user import User
from src.schemas.login import Login
from cryptography.fernet import Fernet
from datetime import datetime
import os
from dotenv import load_dotenv

conn = SessionLocal()

load_dotenv()

# key = Fernet.generate_key()
# print(f"Generated Fernet key: {key.decode()}")
key = key = os.getenv('ENCRYPTION_KEY')
print(key)
f = Fernet(key)

user = APIRouter(
    prefix="/user",
    tags=["user"],
)

@user.get("/")
def index():
    result = conn.execute(users.select().where(users.c.status==True)).fetchall()
    data = []
    for row in result:
        user_dict = dict(row._mapping)
        user_dict["created_at"] = user_dict["created_at"].isoformat()
        if user_dict["updated_at"]:
            user_dict["updated_at"] = user_dict["updated_at"].isoformat()
        data.append(user_dict)
    if len(data) == 0:
        return JSONResponse(content={"success": False, "message": "No se encontraron resultados"})
    return JSONResponse(content={"success": True, "message": "Lista de usuarios", "data": data})

@user.post("/")
def store(user: User):
    if user.repeatPassword != user.password:
        return JSONResponse(content={"success": False, "message": "Las contraseñas no coinciden"})
    new_user = {"name":user.name,"email":user.email,"created_at": datetime.now()}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    data = conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al crear el usuario"})
    user_dict = dict(data._mapping)
    user_dict["created_at"] = user_dict["created_at"].isoformat()
    if user_dict["updated_at"]:
        user_dict["updated_at"] = user_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Usuario creado", "data": user_dict})

@user.put("/{id}",response_model=User)
def update(id:str,user: User):
    new_user = {"name":user.name,"email":user.email,"updated_at": datetime.now()}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.update().values(new_user).where(users.c.id == id))
    conn.commit()
    data = conn.execute(users.select().where(users.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "Ocurrió un error al actualizar el usuario"})
    user_dict = dict(data._mapping)
    user_dict["created_at"] = user_dict["created_at"].isoformat()
    if user_dict["updated_at"]:
        user_dict["updated_at"] = user_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Usuario actualizado", "data": user_dict})

@user.get("/{id}")
def show(id:str):
    data = conn.execute(users.select().where(users.c.id == id)).first()
    if data is None:
        return JSONResponse(content={"success": False, "message": "No se encontró al usuario"})
    user_dict = dict(data._mapping)
    user_dict["created_at"] = user_dict["created_at"].isoformat()
    if user_dict["updated_at"]:
        user_dict["updated_at"] = user_dict["updated_at"].isoformat()
    return JSONResponse(content={"success": True, "message": "Usuario encontrado", "data": user_dict})

@user.delete("/{id}")
def destroy(id:str):
    result = conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return JSONResponse(content={"success": True, "message": "Usuario eliminado"})

@user.post("/login")
def login(login: Login):
    user_search = conn.execute(users.select().where((users.c.name == login.email) | (users.c.email == login.email))).first()
    if user_search is None:
        return JSONResponse(content={"success": False, "message": "Credenciales inválidas", "data": {"email": True}})
    user_search = dict(user_search._mapping)
    stored_encrypted_password = user_search['password']
    stored_password = f.decrypt(stored_encrypted_password).decode()
    
    if stored_password != login.password:
        return JSONResponse(content={"success": False, "message": "Contraseña incorrecta", "data": {"password": True}})
    return JSONResponse(content={"success": True, "message": "Login exitoso", "data": user_search["id"]})