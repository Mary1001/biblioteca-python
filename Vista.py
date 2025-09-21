def mostrar_menu():
    print("\n=== Gestor de LIBROS ===")
    print("📒 1. Agregar LIBRO")
    print("📃 2. Listar LIBROS")
    print("📑 3. Actualizar LIBRO")
    print("🗑️ 4. Eliminar LIBRO")
    print("5. Salir")
    return input("Seleccione una opción: ")

def pedir_datos_libro():
    return {
        "id": int(input("ID: ")),
        "nombreLibro": input("Nombre del libro: "),
        "autor": input("Autor: "),
        "casaEditorial": input("Casa editorial: "),
        "edicion": input("Edición: "),
        "isbn": input("ISBN: ")
    }

def pedir_datos_alumno():
    return {
        "id" : int(input("Ingrese el ID del ALUMNO : ")),
        "nombreAlumno":input("Ingrese el NOMBRE del ALUMNO: "),
        "matricula": input("Ingrese la MATRICULA del ALUMNO: "),
        "gradoGrupo":input("Ingrese el GRADO Y GRUPO del ALUMNO : "),
        "carrera": input("Ingrese la CARRERA del ALUMNO : "),
        "turno": input("Ingrese el TURNO del ALUMNO : "),
        "telefono": input("Ingrese el TELÉFONO del ALUMNO : "),
        "correo": input("Ingrese el CORREO ELECTRONICO del ALUMNO : "),
        "direccion": input("Ingrese la DIRECCION del ALUMNO : "),
        "tutor": input("Ingrese el TUTOR del ALUMNO : ")
    }

def pedir_datos_prestamo():
    return {
        "fecha_prestamo" : input("Ingrese la FECHA del préstamo (DD-MM-AAAA): "),
        "fecha_devolucion" : input("Ingrese la FECHA de devolución (DD-MM-AAAA): ")
    }

def mostrar_libros(lista_libros):
    print("\n📋 Lista de LIBROS:")
    for libro in lista_libros:
        print(f"📚 [{libro['_id']}] {libro['id']} - {libro['nombreLibro']} - {libro['autor']} - {libro['casaEditorial']} - {libro['edicion']} - {libro['isbn']}")

def mostrar_alumnos(lista_alumnos):
    print("\n📋 Lista de ALUMNOS:")
    for alumno in lista_alumnos():
        print(f"📜 [{alumno['_id']}] {alumno['id']} - {alumno['nombreAlumno']} - {alumno['matricula']} - {alumno['gradoGrupo']} - {alumno['carrera']} - {alumno['turno']} - {alumno['telefono']} - {alumno['correo']} - {alumno['direccion']} - {alumno['tutor']}")

def mostrar_prestamos(lista_prestamos):
    print("\n📋 Lista de PRÉSTAMOS:")
    for prestamo in lista_prestamos():
        print(f"📌 Fecha de préstamo: {prestamo['fecha_prestamo']} | Fecha de entrega: {prestamo['fecha_devolucion']}  ")
        print(f"👤 Alumno: {prestamo['alumno']['nombreAlumno']} | Matrícula: {prestamo['alumno']['matricula']} | Grupo: {prestamo['alumno']['gradoGrupo']}")
        print(f"📖 Libro: {prestamo['libro']['nombreLibro']} | Autor: {prestamo['libro']['autor']} | ISBN: {prestamo['libro']['isbn']}")
        print(f"🆔 ID de Préstamo: {prestamo['_id']}")
        print("-" * 50)

