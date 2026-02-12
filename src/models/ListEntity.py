from bson import ObjectId


# Clase genérica para la creación de objetos desde listas y viceversa
class ListEntity:

    # Constructor, tendrá el ID para todas las clases hijo
    def __init__(self, _id: ObjectId):
        self._id: ObjectId = _id if _id else ObjectId()

    # Métodos de clase
    # Añadimos el decorador classmethod para indicar que es un método de clase
    # Devolver el objeto a partir de una lista
    @classmethod
    def from_list(cls, list_data: list):
        return cls(*list_data)

    # Devolver el objeto a partir de un dict
    @classmethod
    def from_dict(cls, dict_data: dict):
        return cls(**dict_data)

    # Métodos "normales"
    # Devolver una lista a partir del objeto
    def to_list(self) -> list:
        return [item for item in vars(self).values()]

    # Devolver un dict de todas las variables a partir del objeto
    def to_dict(self) -> dict:
        # 1. Usamos .copy() para no modificar el objeto original permanentemente
        return vars(self).copy()

    # Comparador
    def __eq__(self, value) -> bool:
        return isinstance(value, ListEntity) and self._id == value._id

    # Mostrar con srt()
    def __str__(self) -> str:
        return self._id

    # Mostrar al printear el objeto
    def __repr__(self) -> str:
        return str(self)
