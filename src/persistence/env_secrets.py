from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import os

# Obtenemos la ruta de la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Clase para cargar los secretos desde un archivo
class Env_secrets(BaseSettings):

    # Añadimos el nombre del secreto como variable
    # y, solo en caso de que no lo encuente, un valor por defecto
    # (en este caso con este valor de ejemplo no conectaría a nada, pero es solo para mostrar la sintaxis)
    db_conn: str = "mongodb+srv://{..."

    # Cargamos la configuración de la clase
    model_config = SettingsConfigDict(
        # Combinamos la ruta base con el nombre del archivo
        env_file=os.path.join(BASE_DIR, ".env"),
        # Esta opción evita errores en caso de que haya variables en .env
        # que estén vacías (por ejemplo cuando hacemos pruebas)
        env_ignore_empty=True,
        # Esta configuración hace que no de error si el archivo
        # tiene variables que no se hayan definido aquí
        # (por defecto "forbid" arroja error si hay variables que no se han pedido)
        extra="ignore",
    )
