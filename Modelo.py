#Modelo Lógico,  Lógica de Negocio, Modelo de negocio 

from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["Biblioteca_4APV_Capas"]
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