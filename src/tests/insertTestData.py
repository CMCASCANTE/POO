from persistence.persistance import Student_DAO, Teacher_DAO, Module_DAO, Cycle_DAO
from models.models import Student, Teacher, Module, Cycle


def insert_test_data():
    # --- 1. CICLOS (Eliminado el ID numérico, se usa el código como identificador) ---
    cycle_dao = Cycle_DAO()
    cycles = [
        # Grado Medio
        Cycle("SMR", "Sistemas Microinformáticos y Redes"),
        # Grado Superior
        Cycle("DAM", "Desarrollo de Aplicaciones Multiplataforma"),
        Cycle("DAW", "Desarrollo de Aplicaciones Web"),
        Cycle("ASIR", "Administración de Sistemas Informáticos en Red"),
        # Cursos de Especialización
        Cycle("CE_CIBER", "Curso de Especialización en Ciberseguridad"),
        Cycle(
            "CE_IA", "Curso de Especialización en Inteligencia Artificial y Big Data"
        ),
    ]
    for c in cycles:
        cycle_dao.insert(c)

    # --- 2. PROFESORES (DNI inventado sustituyendo al ID) ---
    teacher_dao = Teacher_DAO()
    teachers = [
        Teacher("12345678A", "Oscar Profesor", "oscar@fpdrioja.com"),
        Teacher("23456789B", "Maria Experta", "maria@fpdrioja.com"),
        Teacher("34567890C", "Juan Dual", "juan@fpdrioja.com"),
        Teacher("45678901D", "Elena Código", "elena@fpdrioja.com"),
        Teacher("56789012E", "Roberto Redes", "roberto@fpdrioja.com"),
        Teacher("67890123F", "Lucía Lógica", "lucia@fpdrioja.com"),
        Teacher("78901234G", "Andrés Analítica", "andres@fpdrioja.com"),
        Teacher("89012345H", "Sara Seguridad", "sara@fpdrioja.com"),
    ]
    for t in teachers:
        teacher_dao.insert(t)

    # --- 3. MÓDULOS (ID sustituido por iniciales del nombre) ---
    module_dao = Module_DAO()
    modules = [
        # SMR (Ciclo SMR)
        Module("MME", "Montaje y Mantenimiento de Equipos", "SMR", "12345678A"),
        Module("SOM", "Sistemas Operativos Monopuesto", "SMR", "56789012E"),
        Module("RL", "Redes Locales", "SMR", "56789012E"),
        Module("AO", "Aplicaciones Ofimáticas", "SMR", "34567890C"),
        # DAM (Ciclo DAM)
        Module("SI", "Sistemas Informáticos", "DAM", "12345678A"),
        Module("BD", "Bases de Datos", "DAM", "23456789B"),
        Module("PROG", "Programación", "DAM", "12345678A"),
        Module("ED", "Entornos de Desarrollo", "DAM", "45678901D"),
        Module("AD", "Acceso a Datos", "DAM", "23456789B"),
        Module("DI", "Desarrollo de Interfaces", "DAM", "45678901D"),
        Module(
            "PMM", "Programación Multimedia y Dispositivos Móviles", "DAM", "67890123F"
        ),
        Module("SGE", "Sistemas de Gestión Empresarial", "DAM", "67890123F"),
        # DAW (Ciclo DAW)
        Module("DWEC", "Desarrollo Web Entorno Cliente", "DAW", "34567890C"),
        Module("DWES", "Desarrollo Web Entorno Servidor", "DAW", "23456789B"),
        Module("DAW", "Despliegue de Aplicaciones Web", "DAW", "34567890C"),
        Module("DIW", "Diseño de Interfaces Web", "DAW", "45678901D"),
        # ASIR (Ciclo ASIR)
        Module("ASO", "Administración de Sistemas Operativos", "ASIR", "12345678A"),
        Module("SRI", "Servicios de Red e Internet", "ASIR", "56789012E"),
        Module("IAW", "Implantación de Aplicaciones Web", "ASIR", "67890123F"),
        Module("SAD", "Seguridad y Alta Disponibilidad", "ASIR", "89012345H"),
        # CE Ciberseguridad (Ciclo CE_CIBER)
        Module("BRS", "Bastionado de Redes y Sistemas", "CE_CIBER", "89012345H"),
        Module("HE", "Hacking Ético", "CE_CIBER", "89012345H"),
        Module("AFI", "Análisis Forense Informático", "CE_CIBER", "56789012E"),
        # CE IA y Big Data (Ciclo CE_IA)
        Module("MIA", "Modelos de Inteligencia Artificial", "CE_IA", "78901234G"),
        Module("SBD", "Sistemas de Big Data", "CE_IA", "78901234G"),
        Module("PIAR", "Programación de Inteligencia Artificial", "CE_IA", "78901234G"),
    ]
    for m in modules:
        module_dao.insert(m)

    # --- 4. ALUMNOS (DNI extraído del CSV real aportado) ---
    student_dao = Student_DAO()
    students = [
        Student("00000000A", "Ana Macario", ["SI", "BD", "PROG", "ED"]),  # Alumna DAM
        Student(
            "11111111B", "Carlos Martinez", ["DWEC", "DWES", "DAW", "DIW"]
        ),  # Alumno DAW
        Student(
            "22222222C", "Beatriz Binario", ["SAD", "BRS", "HE"]
        ),  # Alumna ASIR + Ciber
        Student("33333333D", "Diego Doner", ["MME", "SOM", "RL"]),  # Alumno SMR
        Student("44444444E", "Elena Enlace", ["MIA", "SBD", "PIAR"]),  # Alumna IA
        Student(
            "55555555F", "Fernando Frame", ["AD", "DI", "PMM", "SGE"]
        ),  # Alumno DAM 2º
        Student("6666666G", "Gema Gigabyte", ["ASO", "SRI", "IAW"]),  # Alumna ASIR
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
