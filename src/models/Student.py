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
            [Module(mod) for mod in modules.split(";")] if modules else None
        )

    # Debido a que hemos creado una lista de modulos
    # tenemos que modificar la conversión a lista para
    # esta clase, de modo que lo muestre igual que como esta guardado
    def to_list(self) -> list:
        list = [item for item in vars(self).values()]
        list[2] = ";".join([mod._id for mod in list[2]])

        return list

    # Tambien modificamos la conversión a dict
    def to_dict(self) -> dict:
        # Obtenemos las variables del objeto ya en un dict
        stud_dict = vars(self)
        print(stud_dict)
        # Modificamos el valor de modules, si tiene modules
        # para guardarlos como string y mantener la lógica de la app
        if stud_dict["modules"]:
            stud_dict["modules"] = ";".join([str(mod) for mod in stud_dict["modules"]])
        # Devolvemos los datos en un dict ya modificados
        return stud_dict
