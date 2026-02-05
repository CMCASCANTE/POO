from models.models import ListEntity


class DAOI:

    def read(self, entity: ListEntity):
        """Mostrar cualquier objeto"""
        raise NotImplementedError()

    def read_all(self):
        """Mostrar todos los objetos"""
        raise NotImplementedError()

    def insert(self, entity: ListEntity):
        """Inserta cualquier objeto"""
        raise NotImplementedError()

    def update(self, entity: ListEntity):
        """Actualizar cualquier objeto"""
        raise NotImplementedError()

    def delete(self, entity: ListEntity):
        """Elimina cualquier objeto"""
        raise NotImplementedError()
