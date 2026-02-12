from .ListEntity import ListEntity
from bson import ObjectId


# Creación de la clase para los ciclos
class Cycle(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    # El * obliga a introducir el nombre del atributo al crearlo
    def __init__(self, *, _id: ObjectId = None, etiqueta: str = None, name: str = None):
        super().__init__(_id)
        self.etiqueta: str = etiqueta
        self.name: str = name

    # Sobreescribimos Mostrar con srt() para que se muestre la etiqueta
    def __str__(self) -> str:
        return self.etiqueta
