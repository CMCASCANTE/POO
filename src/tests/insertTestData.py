from persistence.persistance import Student_DAO, Teacher_DAO, Module_DAO, Cycle_DAO
from models.models import Student, Teacher, Module, Cycle


def insert_test_data():
    # --- 1. CICLOS ---
    cycle_dao = Cycle_DAO()
    cycles = [
        Cycle(etiqueta="SMR", name="Sistemas Microinformáticos y Redes"),
        Cycle(etiqueta="DAM", name="Desarrollo de Aplicaciones Multiplataforma"),
        Cycle(etiqueta="DAW", name="Desarrollo de Aplicaciones Web"),
        Cycle(etiqueta="ASIR", name="Administración de Sistemas Informáticos en Red"),
        Cycle(etiqueta="CE_CIBER", name="Curso de Especialización en Ciberseguridad"),
        Cycle(
            etiqueta="CE_IA",
            name="Curso de Especialización en Inteligencia Artificial y Big Data",
        ),
    ]
    for c in cycles:
        cycle_dao.insert(c)

    # --- 2. PROFESORES ---
    teacher_dao = Teacher_DAO()
    teachers = [
        Teacher(dni="12345678A", name="Oscar Profesor", email="oscar@fpdrioja.com"),
        Teacher(dni="23456789B", name="Maria Experta", email="maria@fpdrioja.com"),
        Teacher(dni="34567890C", name="Juan Dual", email="juan@fpdrioja.com"),
        Teacher(dni="45678901D", name="Elena Código", email="elena@fpdrioja.com"),
        Teacher(dni="56789012E", name="Roberto Redes", email="roberto@fpdrioja.com"),
        Teacher(dni="67890123F", name="Lucía Lógica", email="lucia@fpdrioja.com"),
        Teacher(dni="78901234G", name="Andrés Analítica", email="andres@fpdrioja.com"),
        Teacher(dni="89012345H", name="Sara Seguridad", email="sara@fpdrioja.com"),
    ]
    for t in teachers:
        teacher_dao.insert(t)

    # --- 3. MÓDULOS ---
    module_dao = Module_DAO()
    modules = [
        # SMR
        Module(
            etiqueta="MME",
            name="Montaje y Mantenimiento de Equipos",
            cycle="SMR",
            teacher="12345678A",
        ),
        Module(
            etiqueta="SOM",
            name="Sistemas Operativos Monopuesto",
            cycle="SMR",
            teacher="56789012E",
        ),
        Module(etiqueta="RL", name="Redes Locales", cycle="SMR", teacher="56789012E"),
        Module(
            etiqueta="AO",
            name="Aplicaciones Ofimáticas",
            cycle="SMR",
            teacher="34567890C",
        ),
        # DAM
        Module(
            etiqueta="SI",
            name="Sistemas Informáticos",
            cycle="DAM",
            teacher="12345678A",
        ),
        Module(etiqueta="BD", name="Bases de Datos", cycle="DAM", teacher="23456789B"),
        Module(etiqueta="PROG", name="Programación", cycle="DAM", teacher="12345678A"),
        Module(
            etiqueta="ED",
            name="Entornos de Desarrollo",
            cycle="DAM",
            teacher="45678901D",
        ),
        Module(etiqueta="AD", name="Acceso a Datos", cycle="DAM", teacher="23456789B"),
        Module(
            etiqueta="DI",
            name="Desarrollo de Interfaces",
            cycle="DAM",
            teacher="45678901D",
        ),
        Module(
            etiqueta="PMM",
            name="Programación Multimedia y Dispositivos Móviles",
            cycle="DAM",
            teacher="67890123F",
        ),
        Module(
            etiqueta="SGE",
            name="Sistemas de Gestión Empresarial",
            cycle="DAM",
            teacher="67890123F",
        ),
        # DAW
        Module(
            etiqueta="DWEC",
            name="Desarrollo Web Entorno Cliente",
            cycle="DAW",
            teacher="34567890C",
        ),
        Module(
            etiqueta="DWES",
            name="Desarrollo Web Entorno Servidor",
            cycle="DAW",
            teacher="23456789B",
        ),
        Module(
            etiqueta="DAW",
            name="Despliegue de Aplicaciones Web",
            cycle="DAW",
            teacher="34567890C",
        ),
        Module(
            etiqueta="DIW",
            name="Diseño de Interfaces Web",
            cycle="DAW",
            teacher="45678901D",
        ),
        # ASIR
        Module(
            etiqueta="ASO",
            name="Administración de Sistemas Operativos",
            cycle="ASIR",
            teacher="12345678A",
        ),
        Module(
            etiqueta="SRI",
            name="Servicios de Red e Internet",
            cycle="ASIR",
            teacher="56789012E",
        ),
        Module(
            etiqueta="IAW",
            name="Implantación de Aplicaciones Web",
            cycle="ASIR",
            teacher="67890123F",
        ),
        Module(
            etiqueta="SAD",
            name="Seguridad y Alta Disponibilidad",
            cycle="ASIR",
            teacher="89012345H",
        ),
        # CE Ciberseguridad
        Module(
            etiqueta="BRS",
            name="Bastionado de Redes y Sistemas",
            cycle="CE_CIBER",
            teacher="89012345H",
        ),
        Module(
            etiqueta="HE", name="Hacking Ético", cycle="CE_CIBER", teacher="89012345H"
        ),
        Module(
            etiqueta="AFI",
            name="Análisis Forense Informático",
            cycle="CE_CIBER",
            teacher="56789012E",
        ),
        # CE IA y Big Data
        Module(
            etiqueta="MIA",
            name="Modelos de Inteligencia Artificial",
            cycle="CE_IA",
            teacher="78901234G",
        ),
        Module(
            etiqueta="SBD",
            name="Sistemas de Big Data",
            cycle="CE_IA",
            teacher="78901234G",
        ),
        Module(
            etiqueta="PIAR",
            name="Programación de Inteligencia Artificial",
            cycle="CE_IA",
            teacher="78901234G",
        ),
    ]
    for m in modules:
        module_dao.insert(m)

    # --- 4. ALUMNOS ---
    student_dao = Student_DAO()
    students = [
        Student(
            dni="00000000A", name="Ana Macario", modules=["SI", "BD", "PROG", "ED"]
        ),
        Student(
            dni="11111111B",
            name="Carlos Martinez",
            modules=["DWEC", "DWES", "DAW", "DIW"],
        ),
        Student(dni="22222222C", name="Beatriz Binario", modules=["SAD", "BRS", "HE"]),
        Student(dni="33333333D", name="Diego Doner", modules=["MME", "SOM", "RL"]),
        Student(dni="44444444E", name="Elena Enlace", modules=["MIA", "SBD", "PIAR"]),
        Student(
            dni="55555555F", name="Fernando Frame", modules=["AD", "DI", "PMM", "SGE"]
        ),
        Student(dni="6666666G", name="Gema Gigabyte", modules=["ASO", "SRI", "IAW"]),
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
