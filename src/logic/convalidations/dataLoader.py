from persistence.persistance import Convalidation_DAO
from models.models import Convalidation


class DataLoader:

    # Función para subir los datos a mongo atlas
    # Recibira una lista de objetos tipo Convalidaion y
    # los subirá a la colección Ci¡onvalidations
    @staticmethod
    def upData(lista_convs: list[Convalidation]):
        # Abrir conexión
        db_con: Convalidation_DAO = Convalidation_DAO()

        # Usamos la funcion de insertar todos de la persistencia
        # Y devolvemos el resultado
        return db_con.insert_all(lista_convs)
