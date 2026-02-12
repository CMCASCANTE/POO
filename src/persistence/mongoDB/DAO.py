from .DAOI import DAOI
from ..env_secrets import Env_secrets
from models.models import ListEntity


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class DAO(DAOI):
    def __init__(self, entity_name: str, entity_class: ListEntity):
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
        self.T: ListEntity = entity_class

    # Metodo READ
    def read(self, entity: ListEntity) -> ListEntity:
        # Comprobamos que el objeto es del tipo correcto
        if isinstance(entity, self.T) is False:
            return None
        # Read
        try:
            # collection.find() devuelve un Cursor, que es un iterador eficiente ;)
            result = self.collection.find_one({"dni": str(entity)})

            # Verificamos si hay documentos y añadimos los resultados convertidos en objetos
            # En caso de que no haya resultados se devolverá la lista tal y como la hemos iniciado, vacía
            if result:
                return self.T.from_dict(result)

            else:
                return None

        except Exception as e:
            print(e)

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
            return None

        return list

    # Metodo INSERT
    def insert(self, entity: ListEntity) -> bool:
        # Comprobamos que el objeto es del tipo correcto
        if isinstance(entity, self.T) is False:
            return False

        # ya que estamos usando objectID como ID, vamos a comprobar
        # antes de insertar si la entidad existe
        # Damos por echo que se le va a pasar un dni, que igualmente debería
        # ser único y así lo indicaremos en nuestro front
        if self.read(entity):
            return False

        # Realizamos el insert de la entidad
        try:
            self.collection.insert_one(entity.to_dict())
            # devolvemos un true si todo ha ido bien
            return True
        except Exception as e:
            return False

    # Método UPDATE
    def update(self, entity: ListEntity) -> bool:
        # Comprobamos que el objeto es del tipo correcto
        if isinstance(entity, self.T) is False:
            return False

        # MongoDB no permite modificar el _id de un documento existente,
        # por lo que ya que estamos usando estos IDs, lo eliminamos del objeto que le hemos pasado
        update_obj = entity.to_dict()
        if "_id" in update_obj:
            del update_obj["_id"]

        # Lanzamos el delete para que coincida con la entidad que se ha proporcionado
        try:
            self.collection.update_one(
                filter={"dni": str(entity)}, update={"$set": update_obj}
            )
            # devolvemos un true si todo ha ido bien
            return True
        except Exception as e:
            return False

    # Método DELETE
    def delete(self, entity: ListEntity) -> bool:
        # Comprobamos que el objeto es del tipo correcto
        if isinstance(entity, self.T) is False:
            return False
        # Realizamos el delete según la entidad
        try:
            self.collection.delete_one({"dni": str(entity)})
            # self.collection.delete_many({"name": "Carlos Martinez"})
            # devolvemos un true si todo ha ido bien
            return True
        except Exception as e:
            return False

    # Cerramos la conexión
    def close(self):
        self.client.close()
