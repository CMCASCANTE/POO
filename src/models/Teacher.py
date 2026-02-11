from .ListEntity import ListEntity
from bson import ObjectId


# Creación de la clase para los profesores
class Teacher(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    def __init__(
        self, _id: ObjectId = None, dni: str = None, name: str = None, email: str = None
    ):
        super().__init__(_id=ObjectId(_id) if _id else ObjectId())
        self.dni: str = dni
        self.name: str = name
        self.email: str = email
