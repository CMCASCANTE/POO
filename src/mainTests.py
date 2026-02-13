from tests.testMongoCRUD import testsPersistence as testsMongo
from tests.insertNormalizationData import normalizar
from models.models import Student

"""
Ejecutable para pruebas
Debido a que son pruebas de funcionamiento,
toda la lógica se encuentra en los archivos 
del directorio tests, icluidos los imports, prints, etc....
"""

##########################
# TESTS DE NORMALIZACIÓN #
##########################

# Lanzamos la normalización y subida de datos a MongoDB
# normalizar()

# Prueba de acceso a datos subidos a MongoDB tras normalizar
stud = Student(_id="11111111B")
print(stud.convalidations)


##################
# TESTS DE MONGO #
##################
tests = testsMongo()

# Inicialización de datos de prueba
# tests.init_test_data()

# Tests de CRUD
tests.testRead()
tests.testInsert()
tests.testUpdate()
tests.testDelete()
