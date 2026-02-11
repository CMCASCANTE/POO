from .ListEntity import ListEntity
from bson import ObjectId


# Creación de la clase para los ciclos
class Cycle(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    def __init__(self, _id: ObjectId = None, etiqueta: str = None, name: str = None):
        super().__init__(_id=ObjectId(_id) if _id else ObjectId())
        self.etiqueta: str = etiqueta
        self.name: str = name
