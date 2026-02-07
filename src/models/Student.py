from .ListEntity import ListEntity
from .Module import Module


# Creación de la clase para los estudiantes
class Student(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    def __init__(self, _id, name: str = None, modules: str = None):
        super().__init__(_id)
        self.name: str = name
        # Los módulos se guardan como un string separado por ; por lo que
        # lo dividimos y guardamos cada uno como un objeto en una lista
        self.modules: list[Module] = (
            [Module(mod) for mod in modules] if modules else None
        )

    def to_dict(self) -> dict:
        # Obtenemos las variables del objeto ya en un dict
        stud_dict = vars(self)
        # Modificamos el valor de modules, si tiene modules
        # para guardarlos como string ya que mongo no puede guardar listas de objetos
        if stud_dict["modules"]:
            stud_dict["modules"] = [str(mod) for mod in stud_dict["modules"]]
        # Devolvemos los datos en un dict ya modificados
        return stud_dict
