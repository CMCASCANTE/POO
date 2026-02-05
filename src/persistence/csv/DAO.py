from .DAOI import DAOI
from models.models import ListEntity
import csv


class DAO(DAOI):
    def __init__(self, entity_file: str, entity_class: ListEntity):
        # Definimos la ruta del archivo CSV según el tipo de entidad que indiquemos
        self.file: str = f"../assets/{entity_file}.csv"
        # Definimos la clase de la entidad correspondiente para las operaciones
        self.T: ListEntity = entity_class

    # Metodo SELECT
    def select(self, entity: ListEntity) -> ListEntity:
        # Creamos una lista en la que vamos a almacenar las filas del csv
        list = []

        # Abrimos la "Tabla" correspondiente y guardamos sus filas en la lista según su tipo
        with open(self.file, "r", encoding="utf-8", newline="") as file:
            # Eliminamos el salto de línea y guardamos las líneas en data
            data = [line.strip() for line in file.readlines()]
            # Creamos los objetos correspondientes y los añadimos a la lista
            list = [
                self.T.from_list(obj) for obj in [elm.split(",") for elm in data[1:]]
            ]

        # Recorremos la lista de elementos y devolvemos el primer resultado
        # ya que se supone que los ids son únicos...
        return [elm for elm in list if elm == entity][0]

    # Metodo INSERT
    def insert(self, entity: ListEntity) -> bool:
        # Definimos una lista para guardar los datos
        rows = []

        # Comprobamos que el objeto es del tipo correcto
        if isinstance(entity, self.T) is False:
            return False

        # Leemos todo el archivo y guardamos las filas en una lista
        with open(self.file, "r", encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))

        # Comprobamos si el ID ya está en la lista, de ser así devolvemos false
        entity_data = entity.to_list()
        if any(row[0] == str(entity_data[0]) for row in rows[1:]):
            return False

        # Añadimos el nuevo dato a la lista
        rows.append(entity_data)

        # Sobrescribimos el archivo con los datos actualizados
        # ** Es mas eficiente usar el modo append ("a") pero me ha estado dando error al no respetar la ultima línea **
        with open(self.file, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        # Devolvemos true al finalizar la inserción
        return True

    # Metodo UPDATE
    def update(self, entity: ListEntity) -> bool:
        # Comprobamos que el objeto es del tipo correcto
        if isinstance(entity, self.T) is False:
            return False

        # Creamos una lista para almacenar los datos y un booleano para saber si se ha actualizado algo
        rows = []
        updated = False
        # Guardamos el id de la entidad a actualizar
        entity_id = entity.to_list()[0]

        # Leemos todo el archivo y guardamos la cabecera y los datos por separado
        with open(self.file, "r", encoding="utf-8", newline="") as file:
            reader = list(csv.reader(file))
            header = reader[0]
            data = reader[1:]

        # Guardamos la cabecera en la lista de datos
        # Buscamos el ID y si lo encuentra añadimos la entidad actualizada convertida en lista marcando que se ha actualizado
        # En caso de que no lo encuentre, añadimos la fila original
        rows.append(header)
        for row in data:
            if row[0] == str(entity_id):
                rows.append(entity.to_list())
                updated = True
            else:
                rows.append(row)

        # si se ha realizado alguna actualización, escribimos los datos de nuevo en el archivo
        if updated:
            with open(self.file, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        # devolvemos el booleano que indica si se ha actualizado algo
        return updated

    # Metodo DELETE
    def delete(self, entity: ListEntity) -> bool:
        # Creamos una lista para almacenar los datos y un booleano para saber si se ha eliminado algo
        rows = []
        deleted = False

        # Leemos todo el archivo y guardamos la cabecera y los datos por separado
        with open(self.file, "r", encoding="utf-8", newline="") as file:
            reader = list(csv.reader(file))
            header = reader[0]
            data = reader[1:]

        # Guardamos la cabecera en la lista de datos
        # Buscamos el ID y si lo encuentra, marcamos que se ha eliminado y no añadimos esa fila a la lista
        # En caso de que no lo encuentre, añadimos la fila original
        rows.append(header)
        for row in data:
            if row[0] == entity._id:
                deleted = True
            else:
                rows.append(row)

        # si se ha realizado alguna eliminación, escribimos los datos de nuevo en el archivo
        if deleted:
            with open(self.file, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        # devolvemos el booleano que indica si se ha eliminado algo
        return deleted

    # Metodo SELECT ALL
    def select_all(self) -> list:
        # Creamos una lista en la que vamos a almacenar las filas del csv
        list = []

        # Abrimos la "Tabla" correspondiente y guardamos sus filas en la lista según su tipo
        with open(self.file, "r", encoding="utf-8", newline="") as file:
            # Eliminamos el salto de línea y guardamos las líneas en data
            data = [line.strip() for line in file.readlines()]
            # Creamos los objetos correspondientes y los añadimos a la lista
            list = [
                self.T.from_list(obj) for obj in [elm.split(",") for elm in data[1:]]
            ]

        # Devolvemos la lista de objetos
        return list
