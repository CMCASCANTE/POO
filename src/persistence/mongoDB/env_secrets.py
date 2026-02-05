from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import os

# Obtenemos la ruta de la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


# Clase para cargar los secretos desde un archivo
class Env_secrets(BaseSettings):

    # Añadimos el nombre del secreto como variable
    # y, solo en caso de que no lo encuente, un valor por defecto
    # (api_key solo es un ejemplo, no se esta usando actualmente)
    api_key: str = "mi_api"

    # Si no queremos un valor por defecto, no ponemos nada, de manera
    # que obligamos a que se defina en el .env (ya se gestionará despues
    # si puede definirse vacía o no)
    db_user: str
    db_pass: str

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
