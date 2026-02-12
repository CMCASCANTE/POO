from .ListEntity import ListEntity
from .Cycle import Cycle
from .Teacher import Teacher
from bson import ObjectId


# Creación de la clase para los modulos
class Module(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    # El * obliga a introducir el nombre del atributo al crearlo
    def __init__(
        self,
        *,
        _id: ObjectId = None,
        etiqueta: str = None,
        name: str = None,
        cycle: str = None,
        teacher: str = None,
    ):
        super().__init__(_id)
        self.etiqueta: str = etiqueta
        self.name: str = name
        self.cycle: Cycle = Cycle(etiqueta=cycle) if cycle else None
        self.teacher: Teacher = Teacher(dni=teacher) if teacher else None

    # Para poder introducir los datos en Mongo, es necesario que sean de tipo simple
    # por lo que modificamos los  objetos de ciclos y profesores a string
    def to_dict(self) -> dict:
        # 1. Usamos .copy() para no modificar el objeto original permanentemente
        module_dict = vars(self).copy()
        # Modificamos el valor del id de ciclos y profesores, si tiene
        # para guardarlos como string y mantener la lógica de la app
        if module_dict["cycle"]:
            module_dict["cycle"] = str(module_dict["cycle"])

        if module_dict["teacher"]:
            module_dict["teacher"] = str(module_dict["teacher"])
        # Devolvemos los datos en un dict ya modificados
        return module_dict

    # Sobreescribimos Mostrar con srt() para que se muestre la etiqueta
    def __str__(self) -> str:
        return self.etiqueta if isinstance(self.etiqueta, str) else "Desconocido"
