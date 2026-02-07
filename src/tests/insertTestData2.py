from persistence.persistance import Student_DAO, Teacher_DAO, Module_DAO, Cycle_DAO
from models.models import Student, Teacher, Module, Cycle


def insert_test_data():
    # --- 1. CICLOS ---
    cycle_dao = Cycle_DAO()
    cycles = [
        Cycle("1", "Desarrollo de Aplicaciones Multiplataforma (DAM)"),
        Cycle("2", "Desarrollo de Aplicaciones Web (DAW)"),
        Cycle("3", "Administración de Sistemas Informáticos en Red (ASIR)"),
    ]
    for c in cycles:
        cycle_dao.insert(c)

    # --- 2. PROFESORES ---
    teacher_dao = Teacher_DAO()
    teachers = [
        Teacher("1", "Oscar Profesor", "oscar@fpdrioja.com"),
        Teacher("2", "Maria Experta", "maria@fpdrioja.com"),
        Teacher("3", "Juan Dual", "juan@fpdrioja.com"),
        Teacher("4", "Elena Código", "elena@fpdrioja.com"),
    ]
    for t in teachers:
        teacher_dao.insert(t)

    # --- 3. MÓDULOS ---
    module_dao = Module_DAO()
    modules = [
        Module("1", "Sistemas Informáticos", "1", "1"),
        Module("2", "Bases de Datos", "1", "2"),
        Module("3", "Programación", "1", "1"),
        Module("4", "Entornos de Desarrollo", "1", "4"),
        Module("5", "Desarrollo Web Cliente", "2", "3"),
        Module("6", "Desarrollo Web Servidor", "2", "2"),
        Module("7", "Despliegue de Aplicaciones", "2", "3"),
        Module("8", "Seguridad y Alta Disponibilidad", "3", "4"),
    ]
    for m in modules:
        module_dao.insert(m)

    # --- 4. ALUMNOS ---
    student_dao = Student_DAO()
    students = [
        Student("1", "Ana Macario", ["1", "2", "3"]),
        Student("2", "Carlos Martinez", ["3", "5", "6"]),
        Student("3", "Beatriz Binario", ["8"]),
        Student("4", "Diego Doner", ["2", "6"]),
    ]
    for s in students:
        student_dao.insert(s)

    # --- VERIFICACIÓN DE TODAS LAS TABLAS ---
    daos_to_verify = [
        ("CICLOS", cycle_dao),
        ("PROFESORES", teacher_dao),
        ("MÓDULOS", module_dao),
        ("ALUMNOS", student_dao),
    ]

    print("\n" + "=" * 50)
    print("VERIFICACIÓN DE MIGRACIÓN A MONGODB")
    print("=" * 50)

    for nombre, dao in daos_to_verify:
        print(f"\n>>> TABLA: {nombre}")
        try:
            registros = dao.read_all()
            if not registros:
                print("No se encontraron registros.")
            else:
                for r in registros:
                    # Usamos to_dict() para mostrar la información limpia
                    print(r.to_dict())
        except Exception as e:
            print(f"Error al leer la tabla {nombre}: {e}")

    print("\n" + "=" * 50)
    print("FIN DE LA VERIFICACIÓN")
