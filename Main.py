from Controlador import agregar_libro, agregar_alumno, agregar_prestamo, listar_libros, listar_alumnos, listar_prestamos, actualizar_libro, actualizar_alumno, eliminar_libro, eliminar_alumno, eliminar_prestamo
from Vista import mostrar_menu


def menu_principal():
    while True:
        print("\n📘 === MENÚ PRINCIPAL DE BIBLIOTECA ===")
        print("1. Agregar LIBRO")
        print("2. Agregar ALUMNO")
        print("3. Agregar PRÉSTAMO")
        print("4. Listar LIBROS")
        print("5. Listar ALUMNOS")
        print("6. Listar PRÉSTAMOS")
        print("7. Actualizar LIBROS")
        print("8. Actualizar ALUMNOS")
        print("9. Eliminar LIBRO")
        print("10. Eliminar ALUMNO")
        print("11. Eliminar PRÉSTAMO")
        print("12. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            agregar_alumno()
        elif opcion == "3":
            agregar_prestamo()
        elif opcion == "4":
            listar_libros()
        elif opcion == "5":
            listar_alumnos()
        elif opcion == "6":
            listar_prestamos()
        elif opcion == "7":
            actualizar_libro()
        elif opcion == "8":
            actualizar_alumno()
        elif opcion == "9":
            eliminar_libro()
        elif opcion == "10":
            eliminar_alumno()
        elif opcion == "11":
            eliminar_prestamo()
        elif opcion == "12":
            print("👋 Cerrando el sistema...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()