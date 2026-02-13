from .ListEntity import ListEntity
from .Module import Module


# Creación de la clase para los estudiantes
class Student(ListEntity):

    # Constructor de la clase(con los atributos que hemos definido)
    # El * obliga a introducir el nombre del atributo al crearlo
    def __init__(
        self,
        *,
        _id: str = None,
        name: str = None,
        modules: str = None,
    ):
        super().__init__(_id)
        self.name: str = name
        # Los módulos se guardan como un string separado por ; por lo que
        # lo dividimos y guardamos cada uno como un objeto en una lista
        self.modules: list[Module] = (
            [Module(_id=mod) for mod in modules] if modules else None
        )

    # Función para cargar las convalidaciones del alumno
    @property
    def convalidations(self):
        from logic.logic import ListConvalidations

        # Sacamos la lista de convalidaciones de la lógica y la guardamos
        convalidations = ListConvalidations()

        return convalidations.lista_convalidations_student(self)

    def to_dict(self) -> dict:
        # Obtenemos las variables del objeto ya en un dict
        stud_dict = vars(self)
        # Modificamos el valor de modules, si tiene modules
        # para guardarlos como string ya que mongo no puede guardar listas de objetos
        if stud_dict["modules"]:
            stud_dict["modules"] = [str(mod) for mod in stud_dict["modules"]]
        # Devolvemos los datos en un dict ya modificados
        return stud_dict
