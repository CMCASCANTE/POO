from .Cycle import Cycle
from .Module import Module
from .Status import Status
from .ListEntity import ListEntity
from bson import ObjectId


# Clase para la gestión de las convalidaciones
class Convalidation(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    def __init__(
        self,
        *,
        _id: ObjectId = None,
        alumno: str = None,
        dni: str = None,
        ciclo: Cycle = None,
        modulo: Module = None,
        nota: str = None,
    ):
        super().__init__(_id)
        self.alumno: str = alumno
        self.dni: str = dni
        self.ciclo: Cycle = Cycle(_id=ciclo)
        self.modulo: Module = Module(_id=modulo)
        self.nota: str = nota

    # Definimos estado como propiedad para que se calcule automáticamente a partir de la nota,
    # y que se calcule solo cuando se pida, de modo que se actualice si cambia la nota
    @property
    def estado(self):
        return Status(self.nota)

    # Para poder introducir los datos en Mongo, es necesario que sean de tipo simple
    # por lo que modificamos los  objetos de ciclos y profesores a string
    def to_dict(self) -> dict:
        # 1. Usamos .copy() para no modificar el objeto original permanentemente
        conv_dict = vars(self).copy()
        # Modificamos el valor del id de ciclos y profesores, si tiene
        # para guardarlos como string y mantener la lógica de la app
        if conv_dict["ciclo"]:
            conv_dict["ciclo"] = str(conv_dict["ciclo"])

        if conv_dict["modulo"]:
            conv_dict["modulo"] = str(conv_dict["modulo"])
        # Devolvemos los datos en un dict ya modificados
        return conv_dict

    # Sobreescribimos el método str para mostrarlo como queremos
    def __str__(self):
        return f"{self.modulo} - {self.estado}"

    def __repr__(self):
        return str(self)
