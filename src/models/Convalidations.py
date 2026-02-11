from .Cycle import Cycle
from .Module import Module
from .Status import Status
from .ListEntity import ListEntity
from bson import ObjectId


class Convalidation(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    # El id puede ser none ya que se creará desde el resto de atributos
    # y se pueden crear elementos solo con el dni por ejemplo, para buscar
    def __init__(
        self,
        alumno: str = None,
        dni: str = None,
        ciclo: Cycle = None,
        modulo: Module = None,
        nota: str = None,
        estado: Status = None,
    ):
        super().__init__(_id=ObjectId())
        self.alumno: str = alumno
        self.dni: str = dni
        self.ciclo: Cycle = Cycle(ciclo)
        self.modulo: Module = Module(modulo)
        self.nota: str = nota
        self.estado: Status = Status(nota) if estado == None else estado

    # Para poder introducir los datos en Mongo, es necesario que sean de tipo simple
    # por lo que modificamos los  objetos de ciclos y profesores a string
    def to_dict(self) -> dict:
        # 1. Usamos .copy() para no modificar el objeto original permanentemente
        conv_dict = vars(self).copy()
        # Modificamos el valor del id de ciclos y profesores, si tiene
        # para guardarlos como string y mantener la lógica de la app
        conv_dict["ciclo"] = str(conv_dict["ciclo"]) if conv_dict["ciclo"] else None
        conv_dict["modulo"] = str(conv_dict["modulo"]) if conv_dict["modulo"] else None

        # Lo mismo para el estado
        conv_dict["estado"] = str(conv_dict["estado"]) if conv_dict["estado"] else None

        # Devolvemos los datos en un dict ya modificados
        return conv_dict

    def __str__(self):
        return f"{self.modulo._id} - {self.estado}"

    def __repr__(self):
        return str(self)
