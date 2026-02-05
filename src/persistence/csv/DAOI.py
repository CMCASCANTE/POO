from models.models import ListEntity


class DAOI:

    def insert(self, entity: ListEntity):
        """Inserta cualquier objeto"""
        raise NotImplementedError()

    def select(self, entity: ListEntity):
        """Mostrar cualquier cosa"""
        raise NotImplementedError()

    def update(self, entity: ListEntity):
        """Actualizar cualquier objeto"""
        raise NotImplementedError()

    def delete(self, entity: ListEntity):
        """Elimina cualquier objeto"""
        raise NotImplementedError()

    def select_all(self):
        """Selecciona todos los objetos"""
        raise NotImplementedError()
