from logic.logic import DataCleaner, upData


def normalizar():
    # Normalización de datos
    data = DataCleaner("ejemplo.xlsx")
    # Subida de datos a MongoDB
    upData(data.normalize())
