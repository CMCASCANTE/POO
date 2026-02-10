import pandas as pd
import numpy as np
import re
from typing import Optional


class DataCleaner:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df: Optional[pd.DataFrame] = None

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

    def normalize(self) -> pd.DataFrame:
        if self.df is None:
            self.load_data()

        # 1. Sustituir blancos/espacios por NaN
        df_cleaned = self.df.replace(r"^\s*$", np.nan, regex=True)

        # 2. Identificar columnas fijas (Alumno, DNI, Ciclo)
        cols = df_cleaned.columns.tolist()
        id_vars = [c for c in cols if c.upper() in ["ALUMNO", "DNI", "CICLO"]]

        # 3. Extraer pares de Módulos y Notas
        fragments = []
        # Buscamos columnas MOD1, MOD2, etc.
        mod_cols = [c for c in cols if re.search(r"MOD\d+", c, re.IGNORECASE)]

        for col_mod in mod_cols:
            num = re.search(r"\d+", col_mod).group()
            # Buscamos la nota que le corresponde (nota_modX o nota-modX)
            col_nota = next(
                (c for c in cols if "NOTA" in c.upper() and c.endswith(num)), None
            )

            if col_nota:
                temp_df = df_cleaned[id_vars + [col_mod, col_nota]].copy()
                temp_df.columns = id_vars + ["Modulo", "Nota"]
                fragments.append(temp_df)

        # 4. Unificar y limpiar filas donde no hay módulo solicitado
        if not fragments:
            raise ValueError(f"No se encontraron módulos. Columnas detectadas: {cols}")

        df_normalized = pd.concat(fragments, ignore_index=True)
        # Eliminamos filas donde el módulo sea nulo
        df_normalized = df_normalized.dropna(subset=["Modulo"])

        self.df = df_normalized.reset_index(drop=True)
        return self.df

    def save_to_csv(self, output_path: str):
        if self.df is not None:
            self.df.to_csv(output_path, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    # Importante: Asegúrate de tener instalada la librería openpyxl
    cleaner = DataCleaner("assets/ejemplo.xlsx")
    try:
        df_result = cleaner.normalize()
        print("✅ Archivo detectado como Excel y normalizado correctamente.")
        print(f"Registros finales: {len(df_result)}")
        print(df_result.head())
        cleaner.save_to_csv("datos_normalizados.csv")
    except Exception as e:
        print(f"❌ Error: {e}")
