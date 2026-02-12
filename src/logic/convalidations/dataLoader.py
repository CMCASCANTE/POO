from persistence.persistance import Convalidation_DAO


# Función para subir los datos (se tienen que limpiar primero)
# a mongo atlas
def upData(data: list[dict]):
    # Abrir conexión
    db_con: Convalidation_DAO = Convalidation_DAO()

    # Metemos todos los dicts en mongodb y devolvemso el resultado
    return db_con.insert_all(data)
