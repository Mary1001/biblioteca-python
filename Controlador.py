from Modelo import insertar_libro, insertar_alumno, insertar_prestamo, obtener_libros, obtener_alumnos, obtener_prestamos, actualizar_libro_por_id, actualizar_alumno_por_id, eliminar_libro_por_id, eliminar_alumno_por_id, eliminar_prestamo_por_id
from Vista import pedir_datos_libro, pedir_datos_alumno, pedir_datos_prestamo, mostrar_libros, mostrar_alumnos, mostrar_prestamos,  mostrar_menu
from bson import ObjectId

def agregar_libro():
    datos = pedir_datos_libro()
    insertar_libro(datos)
    print("✅ LIBRO agregado exitosamente.")

def agregar_alumno():  
    datos = pedir_datos_alumno()
    insertar_alumno(datos)
    print("✅ ALUMNO agregada exitosamente.")

def agregar_prestamo():  
    datos = pedir_datos_prestamo()
    insertar_prestamo(datos)
    print("✅ ALUMNO agregada exitosamente.")

def listar_libros():
    libros = obtener_libros()
    mostrar_libros(libros)

def listar_alumnos():
    alumnos = obtener_alumnos()
    mostrar_alumnos(alumnos)

def listar_prestamos():
    prestamos = obtener_prestamos()
    mostrar_prestamos(prestamos)

def actualizar_libro():
    listar_libros()
    object_id = input("ID del libro a actualizar: ")
    id_actualizado=int(input("Ingresa el ID ACTUALIZADO:   "))
    nombrelibro_actualizado=input("Ingresa el NOMBRE DEL LIBRO ACTUALIZADO:   ")
    autor_actualizado=input(" Ingresa el AUTOR ACTUALIZADO:   ")
    casaeditorial_actualizada=input("Ingresa la CASA EDITORIAL ACTUALIZADA:   ")
    edicion_actualizada=input("Ingresa la EDICIÓN ACTUALIZADA:   ")
    isbn_actualizado=input("Ingresa el ISBN ACTUALIZADO:   ")        
    resultado = actualizar_libro_por_id(object_id, id_actualizado, nombrelibro_actualizado, autor_actualizado, casaeditorial_actualizada, edicion_actualizada, isbn_actualizado )
    if resultado.modified_count >= 0:
        print(f"✅ LIBRO actualizado.")
    else:
        print(f"❌ No se encontró un LIBRO con ese ID.")
    
def actualizar_alumno():
    listar_alumnos()
    id_libro=input("Ingresa EL ID del ALUMNO que quieras ACTUALIZAR:   ")
    try:
        object_id = ObjectId(id_libro)
        print(" \n Actualiza los campos    ")
        id_actualizado=int(input("Ingresa el ID ACTUALIZADO:   "))
        nombreAlumno_actualizado=input("Ingresa el NOMBRE DEL ALUMNO ACTUALIZADO:   ")
        matricula_actualizado=input("Ingresa la MATRICULA ACTUALIZADA:   ")
        gradoGrupo_actualizada=input("Ingresa el GRADO Y GRUPO ACTUALIZADO:   ")
        carrera_actualizada=input("Ingresa la CARRERA ACTUALIZADA:   ")
        turno_actualizado=input("Ingresa el TURNO ACTUALIZADO:   ")
        telefono_actualizado=input("Ingresa el TELEFONO ACTUALIZADO:   ")
        correo_actualizado=input("Ingresa el CORREO ACTUALIZADO:   ")
        direccion_actualizado=input("Ingresa la DIRECCION ACTUALIZADA:   ")
        tutor_actualizado=input("Ingresa el TUTOR ACTUALIZADO:   ")
        resultado = actualizar_alumno_por_id(object_id, id_actualizado, nombreAlumno_actualizado, matricula_actualizado, gradoGrupo_actualizada, carrera_actualizada,turno_actualizado, telefono_actualizado, correo_actualizado, direccion_actualizado, tutor_actualizado)
   
        if resultado.modified_count >= 0:
            print("✅ LIBRO actualizado.")
        else:
            print("❌ No se encontró un LIBRO con ese ID.")
    except:
        print("❌ El ID ingresado no es válido.")


def eliminar_libro():
    listar_libros()
    object_id = input("ID del libro a eliminar: ")
    resultado = eliminar_libro_por_id(object_id)
    if resultado.deleted_count > 0:
        print("🗑️ Libro eliminado.")
    else:
        print("❌ No se encontró un libro con ese ID.")

def eliminar_alumno():
    listar_alumnos()
    object_id = input("ID del alumno a eliminar: ")
    resultado = eliminar_alumno_por_id(object_id)
    if resultado.deleted_count > 0:
        print("🗑️ Alumno eliminado.")
    else:
        print("❌ No se encontró un alumno con ese ID.")

def eliminar_prestamo():
    listar_prestamos()
    object_id = input("ID del prestamo a eliminar: ")
    resultado = eliminar_prestamo_por_id(object_id)
    if resultado.deleted_count > 0:
        print("🗑️ Préstamo eliminado.")
    else:
        print("❌ No se encontró un préstamo con ese ID.")
