from .ListEntity import ListEntity


# Creación de la clase para los ciclos
class Cycle(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    # El * obliga a introducir el nombre del atributo al crearlo
    def __init__(self, *, _id: str, name: str = None):
        super().__init__(_id)
        self.name: str = name
