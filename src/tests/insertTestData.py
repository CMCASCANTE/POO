from persistence.persistance import Student_DAO, Teacher_DAO, Module_DAO, Cycle_DAO
from models.models import Student, Teacher, Module, Cycle
from bson import ObjectId


def insert_test_data():
    # --- 1. CICLOS (Eliminado el ID numérico, se usa el código como identificador) ---
    cycle_dao = Cycle_DAO()
    cycles = [
        # Grado Medio
        Cycle(ObjectId(), "SMR", "Sistemas Microinformáticos y Redes"),
        # Grado Superior
        Cycle(ObjectId(), "DAM", "Desarrollo de Aplicaciones Multiplataforma"),
        Cycle(ObjectId(), "DAW", "Desarrollo de Aplicaciones Web"),
        Cycle(ObjectId(), "ASIR", "Administración de Sistemas Informáticos en Red"),
        # Cursos de Especialización
        Cycle(ObjectId(), "CE_CIBER", "Curso de Especialización en Ciberseguridad"),
        Cycle(
            ObjectId(),
            "CE_IA",
            "Curso de Especialización en Inteligencia Artificial y Big Data",
        ),
    ]
    for c in cycles:
        cycle_dao.insert(c)

    # --- 2. PROFESORES (DNI inventado sustituyendo al ID) ---
    teacher_dao = Teacher_DAO()
    teachers = [
        Teacher(ObjectId(), "12345678A", "Oscar Profesor", "oscar@fpdrioja.com"),
        Teacher(ObjectId(), "23456789B", "Maria Experta", "maria@fpdrioja.com"),
        Teacher(ObjectId(), "34567890C", "Juan Dual", "juan@fpdrioja.com"),
        Teacher(ObjectId(), "45678901D", "Elena Código", "elena@fpdrioja.com"),
        Teacher(ObjectId(), "56789012E", "Roberto Redes", "roberto@fpdrioja.com"),
        Teacher(ObjectId(), "67890123F", "Lucía Lógica", "lucia@fpdrioja.com"),
        Teacher(ObjectId(), "78901234G", "Andrés Analítica", "andres@fpdrioja.com"),
        Teacher(ObjectId(), "89012345H", "Sara Seguridad", "sara@fpdrioja.com"),
    ]
    for t in teachers:
        teacher_dao.insert(t)

    # --- 3. MÓDULOS (ID sustituido por iniciales del nombre) ---
    module_dao = Module_DAO()
    modules = [
        # SMR (Ciclo SMR)
        Module(
            ObjectId(), "MME", "Montaje y Mantenimiento de Equipos", "SMR", "12345678A"
        ),
        Module(ObjectId(), "SOM", "Sistemas Operativos Monopuesto", "SMR", "56789012E"),
        Module(ObjectId(), "RL", "Redes Locales", "SMR", "56789012E"),
        Module(ObjectId(), "AO", "Aplicaciones Ofimáticas", "SMR", "34567890C"),
        # DAM (Ciclo DAM)
        Module(ObjectId(), "SI", "Sistemas Informáticos", "DAM", "12345678A"),
        Module("BD", "Bases de Datos", "DAM", "23456789B"),
        Module(ObjectId(), "PROG", "Programación", "DAM", "12345678A"),
        Module(ObjectId(), "ED", "Entornos de Desarrollo", "DAM", "45678901D"),
        Module(ObjectId(), "AD", "Acceso a Datos", "DAM", "23456789B"),
        Module(ObjectId(), "DI", "Desarrollo de Interfaces", "DAM", "45678901D"),
        Module(
            ObjectId(),
            "PMM",
            "Programación Multimedia y Dispositivos Móviles",
            "DAM",
            "67890123F",
        ),
        Module(
            ObjectId(), "SGE", "Sistemas de Gestión Empresarial", "DAM", "67890123F"
        ),
        # DAW (Ciclo DAW)
        Module(
            ObjectId(), "DWEC", "Desarrollo Web Entorno Cliente", "DAW", "34567890C"
        ),
        Module(
            ObjectId(), "DWES", "Desarrollo Web Entorno Servidor", "DAW", "23456789B"
        ),
        Module(ObjectId(), "DAW", "Despliegue de Aplicaciones Web", "DAW", "34567890C"),
        Module(ObjectId(), "DIW", "Diseño de Interfaces Web", "DAW", "45678901D"),
        # ASIR (Ciclo ASIR)
        Module(
            ObjectId(),
            "ASO",
            "Administración de Sistemas Operativos",
            "ASIR",
            "12345678A",
        ),
        Module(ObjectId(), "SRI", "Servicios de Red e Internet", "ASIR", "56789012E"),
        Module(
            ObjectId(), "IAW", "Implantación de Aplicaciones Web", "ASIR", "67890123F"
        ),
        Module(
            ObjectId(), "SAD", "Seguridad y Alta Disponibilidad", "ASIR", "89012345H"
        ),
        # CE Ciberseguridad (Ciclo CE_CIBER)
        Module(
            ObjectId(), "BRS", "Bastionado de Redes y Sistemas", "CE_CIBER", "89012345H"
        ),
        Module(ObjectId(), "HE", "Hacking Ético", "CE_CIBER", "89012345H"),
        Module(
            ObjectId(), "AFI", "Análisis Forense Informático", "CE_CIBER", "56789012E"
        ),
        # CE IA y Big Data (Ciclo CE_IA)
        Module(
            ObjectId(),
            "MIA",
            "Modelos de Inteligencia Artificial",
            "CE_IA",
            "78901234G",
        ),
        Module(ObjectId(), "SBD", "Sistemas de Big Data", "CE_IA", "78901234G"),
        Module(
            ObjectId(),
            "PIAR",
            "Programación de Inteligencia Artificial",
            "CE_IA",
            "78901234G",
        ),
    ]
    for m in modules:
        module_dao.insert(m)

    # --- 4. ALUMNOS (DNI extraído del CSV real aportado) ---
    student_dao = Student_DAO()
    students = [
        Student(
            ObjectId(), "00000000A", "Ana Macario", ["SI", "BD", "PROG", "ED"]
        ),  # Alumna DAM
        Student(
            ObjectId(), "11111111B", "Carlos Martinez", ["DWEC", "DWES", "DAW", "DIW"]
        ),  # Alumno DAW
        Student(
            ObjectId(), "22222222C", "Beatriz Binario", ["SAD", "BRS", "HE"]
        ),  # Alumna ASIR + Ciber
        Student(
            ObjectId(), "33333333D", "Diego Doner", ["MME", "SOM", "RL"]
        ),  # Alumno SMR
        Student(
            ObjectId(), "44444444E", "Elena Enlace", ["MIA", "SBD", "PIAR"]
        ),  # Alumna IA
        Student(
            ObjectId(), "55555555F", "Fernando Frame", ["AD", "DI", "PMM", "SGE"]
        ),  # Alumno DAM 2º
        Student(
            ObjectId(), "6666666G", "Gema Gigabyte", ["ASO", "SRI", "IAW"]
        ),  # Alumna ASIR
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
