import os
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

# 1. Cargar variables del .env
load_dotenv()

# 2. Obtener URI
uri = os.getenv("MONGO_URI")

# 3. Conectar Atlas
client = MongoClient(uri)

# 4. Seleccionar base de datos
db = client["mi_biblioteca"]

# 5. (Opcional) Verificar conexión
try:
    print("✅ Conectado a MongoDB Atlas")
    print("Bases de datos disponibles:", client.list_database_names())
except Exception as e:
    print("❌ Error de conexión:", e)

libros = db["libros"]
alumnos = db["alumnos"]  # Nombre de la colección
prestamos = db["prestamos"]

def insertar_libro(libro):
    return libros.insert_one(libro)

def insertar_alumno (alumno):
    return libros.insert_one(alumno)

def insertar_prestamo(prestamo):
    return prestamos.insert_one(prestamo)

def obtener_libros():
    return list(libros.find())

def obtener_alumnos():
    return list(alumnos.find())

def obtener_prestamos():
    return list(prestamos.find())

def actualizar_libro_por_id(object_id, campo, valor):
    return libros.update_one({"_id": ObjectId(object_id)}, {"$set": {campo: valor}})

def actualizar_alumno_por_id(object_id):
    return alumnos.update_one({"_id": ObjectId(object_id)})

def eliminar_alumno_por_id(object_id):
    return alumnos.delete_one({"_id": ObjectId(object_id)})

def eliminar_libro_por_id(object_id):
    return libros.delete_one({"_id": ObjectId(object_id)})

def eliminar_prestamo_por_id(object_id):
    return alumnos.delete_one({"_id": ObjectId(object_id)})

def seleccionar_alumno(alumno):
    return list(alumnos.find(alumno))

def seleccionar_libro(libro):
     return list(alumnos.find(libro))

def seleccionar_alumno(alumno):
    return list(alumnos.find(alumno))

def seleccionar_libro(libro):

     return list(alumnos.find(libro))
