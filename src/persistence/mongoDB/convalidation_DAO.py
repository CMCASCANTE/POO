from persistence.env_secrets import Env_secrets
from models.models import ListEntity, Convalidation


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Clase para la gestión de las convalidaciones en MongoDB
# Sigue las pautas de nombre pero no hereda del DAO principal, ya que va a tener
# métodos específicos
class Convalidation_DAO:
    def __init__(self, entity_name: str = "convalidations"):
        # Cargamos los secretos desde la clase que hemos definido para ello
        # Usamos la excepción de errores para manejarlos en caso de que falten credenciales, etc
        self.secrets: Env_secrets = Env_secrets()
        # Url de conexión para mongo atlas
        self.uri = self.secrets.db_conn
        # Creación de la conexión con mongo
        self.client = MongoClient(self.uri, server_api=ServerApi("1"), tls=True)
        # Definimos la colección en la que vamos a trabajar
        self.collection = self.client["POO"][entity_name]
        # Definimos la clase de la entidad correspondiente para las operaciones
        self.T: ListEntity = Convalidation

    # Metodo INSERT
    def insert_all(self, lista_datos: list[dict]) -> bool:
        # Realizamos el insert de la entidad
        try:
            # Inserción masiva para mayor eficiencia
            if lista_datos:
                result = self.collection.insert_many(lista_datos)
                return result.inserted_ids
            return []

        except Exception as e:
            return e

    # Metodo READ ALL
    def read_all(self, criterio: dict = None) -> list:
        # Creamos una lista en la que vamos a almacenar los resultados
        list = []

        # Read (Todos los resultados)
        try:
            # collection.find() devuelve un Cursor, que es un iterador eficiente
            if criterio:
                results = self.collection.find(criterio)

            else:
                results = self.collection.find()

            # Verificamos si hay documentos y añadimos los resultados convertidos en objetos
            # En caso de que no haya resultados se devolverá la lista tal y como la hemos iniciado, vacía
            if results:
                list = [self.T.from_dict(elm) for elm in results]
        except Exception as e:
            print(e)

        return list
