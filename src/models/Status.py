# Clase para identificar el estado de una convalidación


class Status:

    def __init__(self, nota: str = None):
        self.nota: str = str(nota)

    @property
    def estado(self):
        if self.nota.isdigit() and 5 <= int(self.nota) <= 10:
            return "estimada"

        elif self.nota == "NO":
            return "desestimada"

        else:
            return "recibida"

    def __str__(self):
        return self.estado

    def __repr__(self):
        return str(self)
