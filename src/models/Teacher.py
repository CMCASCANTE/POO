from .ListEntity import ListEntity
from bson import ObjectId


# Creación de la clase para los profesores
class Teacher(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    # El * obliga a introducir el nombre del atributo al crearlo
    def __init__(
        self,
        _id: ObjectId = None,
        *,
        dni: str = None,
        name: str = None,
        email: str = None
    ):
        super().__init__(_id)
        self.dni: str = dni
        self.name: str = name
        self.email: str = email

    # Sobreescribimos Mostrar con srt() para que se muestre el dni
    def __str__(self) -> str:
        return self.dni
