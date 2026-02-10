from .ListEntity import ListEntity


# Creación de la clase para los profesores
class Teacher(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    def __init__(self, dni: str, name: str = None, email: str = None):
        super().__init__(_id=dni)
        self.name: str = name
        self.email: str = email
