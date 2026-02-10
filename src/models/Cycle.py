from .ListEntity import ListEntity


# Creación de la clase para los ciclos
class Cycle(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    def __init__(self, etiqueta: str, name: str = None):
        super().__init__(_id=etiqueta)
        self.name: str = name
