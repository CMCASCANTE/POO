import pandas as pd
import numpy as np
import re
from pathlib import Path
from typing import Optional
from persistence.persistance import DAO
from models.models import Convalidation


# Clase que normalizará el archivo de convalidaciones
class DataCleaner:
    def __init__(self, file_name: str):
        # Guardamos directorio y nombre del archivo a normalizar por separado
        self.folder_path = Path("../assets")
        self.file_name = file_name
        # Unimos para obtener la ruta completa
        self.file_path = self.folder_path / self.file_name
        # Atributo donde se guardará el dataframe a partir del excel
        self.df: Optional[pd.DataFrame] = None

    # función para cargar el excel de manera correcta
    def load_data(self) -> pd.DataFrame:
        """
        Carga el archivo detectando si es un Excel real aunque la extensión confunda.
        """
        try:
            # Forzamos la lectura como Excel ya que el debug mostró cabeceras PK (ZIP/Excel)
            self.df = pd.read_excel(self.file_path)
        except Exception:
            # Si fallara como Excel, intentamos CSV como último recurso
            self.df = pd.read_csv(
                self.file_path, encoding="latin-1", sep=None, engine="python"
            )

        self.df.columns = [str(c).strip() for c in self.df.columns]
        return self.df

    # Definimos la lógica de limpieza de forma independiente
    def limpiar_valor_dato2(self, valor):
        # Manejo de valores nulos (NaN)
        if pd.isna(valor):
            return valor

        # Convertimos a string y normalizamos
        val_str = str(valor).strip().upper()

        # Condición 1: CV o SI -> 5
        if val_str in ["CV", "SI"]:
            return 5

        # Condición 2: Buscar números (ej. CV-6, I-7)
        match = re.search(r"\d+", val_str)
        if match:
            return int(match.group())

        # Condición 3: Cualquier otro caso
        return "NO"

    # Generador de eqtiquetas para nombre de modulos
    def generate_module_label(self, name: str) -> str:
        """
        Convierte el nombre de un modulo en su etiqueta (acrónimo).
        Filtra conectores comunes y caracteres especiales.
        """
        # Si es un nulo o esta vacío devolvemos none
        if pd.isna(name) or not isinstance(name, str) or name.strip() == "":
            return None  # O return "" si prefieres evitar nulos en Mongo
        # Lista de conectores a ignorar en español
        stop_words = {
            "y",
            "e",
            "o",
            "u",
            "de",
            "del",
            "la",
            "las",
            "el",
            "los",
            "en",
            "para",
            "con",
        }

        # Limpiar caracteres especiales y dividir por espacios
        # Usamos regex para quedarnos solo con letras y espacios
        clean_name = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", "", name)
        words = clean_name.split()

        # Filtrar palabras y extraer la primera letra en mayúscula
        label = "".join(
            word[0].upper() for word in words if word.lower() not in stop_words
        )

        return label

    def normalize(self) -> pd.DataFrame:
        if self.df is None:
            self.load_data()

        # Primero: Sustituir CUALQUIER celda vacía o con espacios por None (NaN en pandas)
        self.df = self.df.replace(r"^\s*$", np.nan, regex=True)

        # 1. Identificamos las columnas fijas (las 3 primeras)
        cols_fijas = self.df.columns[:3].tolist()

        # 2. Identificamos las columnas dinámicas (el resto)
        cols_dinamicas = self.df.columns[3:].tolist()

        # 3. Agrupamos las columnas dinámicas en pares
        # Esto crea una lista de listas: [[col4, col5], [col6, col7], ...]
        pares = [cols_dinamicas[i : i + 2] for i in range(0, len(cols_dinamicas), 2)]

        dfs_temporales = []

        for par in pares:
            # Creamos un sub-dataframe con las 3 fijas + el par actual
            # Renombramos las columnas del par para que coincidan al concatenar
            temp_df = self.df[cols_fijas + par].copy()
            temp_df.columns = cols_fijas + ["Modulo", "Nota"]
            dfs_temporales.append(temp_df)

        # 4. Concatenamos todos los bloques verticalmente
        df_final = pd.concat(dfs_temporales, ignore_index=True)

        # 5. Opcional: Eliminar filas donde los datos nuevos estén vacíos (NaN)
        df_final = df_final.dropna(subset=["Modulo", "Nota"], how="all")

        # 6. Aplicamos la función a la columna dato_2
        df_final["Nota"] = df_final["Nota"].apply(self.limpiar_valor_dato2)

        # 7. Modificamos la columna de modulo con la etiqueta que
        # tendremos definida en nuestra base de datos
        df_final["Modulo"] = df_final["Modulo"].apply(self.generate_module_label)

        # **Opcional: Cambiamos el nombre de los campos a minuscula
        df_final.columns = df_final.columns.str.lower()

        # Orient='records' crea una lista de diccionarios: [{col: val}, {col: val}]
        data_dict = df_final(orient="records")

        # Devolvemos el objeto para poder seguir operando con él
        return data_dict
