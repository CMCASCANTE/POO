from tests.testMongo import testsPersistence as testsMongo

"""
Ejecutable para pruebas
Debido a que son pruebas de funcionamiento,
toda la lógica se encuentra en los archivos 
del directorio tests, icluidos los imports, prints, etc....
"""

##################
# TESTS DE MONGO #
##################
tests = testsMongo()

tests.init_test_data()

tests.testRead()
tests.testInsert()
tests.testUpdate()
tests.testDelete()
