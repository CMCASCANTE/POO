"""
Implementa un método que te permita obtener todos los estudiantes a los que se les ha
aceptado una convalidación de un ciclo-módulo determinado. Este método debería
recibir el ciclo y el módulo en cuestión. 1 punto

Implementa un método que te permita, para cada módulo que haya tenido algún
estudiante que haya tenido una convalidación estimada, generar un fichero con el
nombre del ciclo_módulo en formato csv que contenga los nombres de los
estudiantes. 1 punto

OPCIONAL. Implementa dos métodos adicionales para futuras mejoras de la herramienta.

Implementa un método que te permita obtener todas las convalidaciones de un
estudiante en particular. 0.5 puntos

Implementa un método que te permita determinar si todas las convalidaciones de un
estudiante han sido estimadas. 0.5 puntos
"""

from logic.logic import Presentacion
from models.models import Cycle, Module, Student

presentacion: Presentacion = Presentacion()


# Menú de la aplicación
def mostrar_menu():
    print("\n" + "=" * 40)
    print("      GESTOR DE CONVALIDACIONES")
    print("=" * 40)
    print("1. Buscar alumnos por Ciclo y Módulo")
    print("2. Generar reportes CSV por Módulo")
    print("3. Ver convalidaciones de un alumno (DNI)")
    print("4. Comprobar si un alumno tiene todo estimado")
    print("0. Salir")
    print("=" * 40)


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    # Lista de alumnos por módulo
    if opcion == "1":
        ciclo = input("Introduce el código del Ciclo (ej. GA): ").upper()
        modulo = input("Introduce el código del Módulo (ej. TDC): ").upper()
        ciclo_obj = Cycle(_id=ciclo)
        modulo_obj = Module(_id=modulo)
        lista_alumnos = presentacion.alumnosCicloModulo(ciclo_obj, modulo_obj)
        if lista_alumnos:
            print(f"Lista de alúmnos con la convalidación de {modulo} aceptada")
            print(lista_alumnos)
        else:
            print("No se han encontrado alumnos con esa convalidación.")

        input("Pulsa una tecla para continuar...")

    # Exportación a CSV de los modulos
    elif opcion == "2":
        print("")
        print("\nGenerando ficheros CSV...")
        # Desde la lógica imprimeremos por pantalla las exportaciones
        try:
            presentacion.estimadasCSV()
            print("")
            input("Ha finalizado la exportación, pulsa intro para continuar...")
        except Exception as e:
            print("")
            input(
                "No se ha podido realizar la exportación, pulsa una tecla para continuar..."
            )

    # Obtener las ocnvalidaciones de un alumno
    elif opcion == "3":
        print("")
        dni = input("Introduzca el DNI del alumno: ").upper()
        lista_convs = presentacion.convalidaciones_alumno(Student(_id=dni))

        if lista_convs:
            print("")
            print(f"\nConvalidaciones de {lista_convs[0].alumno} ({dni}):")
            for conv in lista_convs:
                print(f"[{conv.ciclo}] {conv.modulo}: {conv.estado}")
            input("Pulsa una tecla para continuar...")
        else:
            print("")
            print("\nNo se encontró ningún alumno con ese DNI.")

    elif opcion == "4":
        print("")
        dni = input("Introduzca el DNI del alumno: ").upper()
        conv = presentacion.todas_convalidadas(Student(_id=dni))
        print("")
        if conv:
            print("Todas las convalidaciones del alumno han sido estimadas")
        else:
            print("No se han convalidado todos los modulos del alumno")

        print("")
        input("Pulsa una tecla para continuar...")

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        input("Opción no válida, pulsa intro para continuar...")
