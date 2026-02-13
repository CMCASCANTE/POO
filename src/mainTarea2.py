from logic.logic import LogicMongo
from models.models import Teacher, Student, Cycle, Module

# cargamos la lógica que vamos a presentar
logic = LogicMongo()

# Creamos un bucle para el menú
while True:
    # Presentación del menú
    print("\n" + "=" * 30)
    print("   MENU DE TAREA02 POO   ")
    print("=" * 30)
    print("1. Ver todos los Ciclos")
    print("2. Ver Módulos de un Ciclo")
    print("3. Ver Profesor de un Módulo")
    print("4. Ver Estudiantes de un Módulo")
    print("5. Ver Expediente (Módulos+Ciclo) de Alumno")
    print("6. Ver quota restante")
    print("0. Salir")

    # Recogemos la entrada de teclado
    opcion = input("\n> Elige una opción: ")

    # Según la opción marcada ejecutamos...
    if opcion == "1":
        print("\n--- Listado de Ciclos ---")
        # Cargamos la función correspondiente que devuelve la lista con todos los ciclos
        lista = logic.get_all_cycles()
        # Recorremos la lista de objetos y mostramos cada uno con la función to_list()
        for ciclo in lista:
            print(f"- {ciclo.to_list()}")

    elif opcion == "2":
        # Obtenemos el ID del ciclo (en caso de no ser válido no se mostrarán resultados)
        id_ciclo = input("Dime la etiqueta del ciclo (ej. ASIR,DAW...): ")
        # Creamos un objeto a partir del ID para comparar en las búsquedas
        ciclo = Cycle(_id=id_ciclo.upper())
        print(f"\n--- Módulos del ciclo: {ciclo} ---")
        # Cargamos la función correspondiente que devuelve la lista con todos los modulos
        lista = logic.get_modules_by_cycle(ciclo)
        # Recorremos la lista de objetos y mostramos cada uno con la función to_list()
        if lista:
            for mod in lista:
                print(f"- {mod.to_list()}")

        else:
            print("No se han encontrado módulos para ese ciclo.")

    elif opcion == "3":
        # Obtenemos el ID del módulo (en caso de no ser válido no se mostrarán resultados)
        id_modulo = input("Dime la etiqueta del módulo (ej. MME, IC...): ")
        modulo = Module(_id=id_modulo.upper())
        print(f"\n--- Profesor del módulo: {modulo} ---")
        # Cargamos la función correspondiente que devuelve el profesor del módulo
        profe = logic.get_teacher_by_module(modulo)
        # Mostramos el profesor con la función to_list() o un mensaje de no encontrado si es None
        if profe:
            print(f"Profesor: {profe.to_list()}")
        else:
            print("Profesor no encontrado.")

    elif opcion == "4":
        # Obtenemos el ID del módulo (en caso de no ser válido no se mostrarán resultados)
        id_modulo = input("Dime la etiqueta del módulo (ej. MME,IC...): ")
        modulo = Module(_id=id_modulo.upper())
        print(f"\n--- Estudiantes en modulo: {modulo} ---")
        # Cargamos la función correspondiente que devuelve la lista con todos los estudiantes
        lista = logic.get_students_by_module(modulo)
        # Recorremos la lista de objetos y mostramos cada uno con la función to_list()
        # Si no hay elementos, no se mostrará nada
        if lista:
            for alumno in lista:
                print(f"- {alumno.to_list()}")
        else:
            print("No hay estudiantes en ese módulo.")

    elif opcion == "5":
        # Obtenemos el ID del alumno (en caso de no ser válido no se mostrarán resultados)
        id_alumno = input("Dime el dni del alumno: ")
        alumno = Student(_id=id_alumno.upper())
        print(f"\n--- Expediente de alumno con dni: {alumno} ---")
        # Cargamos la función correspondiente que devuelve la lista con todos los modulos + ciclos
        lista = logic.get_student_modules_and_cycle(alumno)
        # Recorremos la lista de objetos y mostramos cada uno con la función to_list()
        if lista:
            for item in lista:
                print(f"- {item.to_list()}")
        else:
            print("No se encontró expediente para ese alumno.")

    # Opción extra para ver la quota restante
    elif opcion == "6":
        print(f"\n--- Te queda la siguiente quota: ---")
        print(f"Quota = {logic.get_quota()}")

    # Opción final para salir del menu
    elif opcion == "0":
        print("Adios!")
        break

    # Opción por defecto para cualquier resultado que no sea el esperado
    else:
        print("Opción no válida.")

    # Al final del while (y fuera de los if) para que se ejecute siempre
    # incluimos un input para obligar a que se pare el menu y se pulse enter para continuar
    input("\nPulse Intro para volver al menú...")

    # Tras los resultados, comprobamos la quota
    # y si es 0 o menor, se cierra la aplicación
    if logic.get_quota() <= 0:
        input("\nTu quota ha llegado a 0, pulsa intro pasa salir...")
        break
