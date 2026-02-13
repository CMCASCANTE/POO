from persistence.persistance import Convalidation_DAO
from persistence.persistance import Student_DAO
from models.models import Cycle, Module, Convalidation, Student
from bson import ObjectId
import pandas as pd
import os


class Presentacion:

    # Función para mostrar todos los alumnos que cumplen la condición
    def alumnosCicloModulo(self, ciclo: Cycle, modulo: Module):
        # Creamos las conexiones que vamos a necesitar con la BBDD
        conn_conv = Convalidation_DAO()
        conn_stud = Student_DAO()
        # Creamos el criterio para la búsqueda de las convalidaciones, en base a los objetos
        criterio = {"modulo": str(modulo), "ciclo": str(ciclo)}
        # Creamos una lista de convalidaciones que cumplan con los criterios
        lista_convalidaciones: list[Convalidation] = conn_conv.read_all(criterio)
        # Creamos la lista de estudiantes a partir de un set de dnis
        # de las convalidaciones para que no se repitan los resultados
        # Y solo cogemos aqueyas cuyo estado sea "estimada"
        lista_estudiantes: list[Student] = [
            conn_stud.read(Student(_id=dni))
            for dni in {
                obj.dni
                for obj in lista_convalidaciones
                if str(obj.estado) == "estimada"
            }
        ]

        # Devolvemos la lista de estudiantes (comprobando que exista,
        # por si ha devuelto algún nulo, que no debería pero...)
        return [f"{stud} - {stud.name}" for stud in lista_estudiantes if stud]

    # Función para crear csvs en base a los modulos convalidados
    def estimadasCSV(self):
        conn = Convalidation_DAO()

        lista_estaminadas = [
            conv for conv in conn.read_all() if str(conv.estado) == "estimada"
        ]

        # Agrupamos los datos en un diccionario: { "nombre_modulo": [lista_de_dicts_alumnos] }
        agrupado = {}

        for conv in lista_estaminadas:
            # Usamos la etiqueta del módulo como nombre de archivo
            nombre_modulo = conv.modulo if conv.modulo else "Desconocido"

            if nombre_modulo not in agrupado:
                agrupado[nombre_modulo] = []

            # Añadimos solo la información que queremos en el CSV
            agrupado[nombre_modulo].append({"DNI": conv.dni, "Alumno": conv.alumno})

        # Indicamos la ruta donde se van a guardar
        ruta_base = os.path.join("..", "assets", "modulos")
        # Creamos un CSV por cada grupo encontrado

        for modulo, alumnos in agrupado.items():
            if alumnos:
                # Generamos los archivos y los creamos con pandas
                df = pd.DataFrame(alumnos)
                nombre_archivo = f"{modulo}.csv"
                ruta_completa = os.path.join(ruta_base, nombre_archivo)
                df.to_csv(ruta_completa, index=False, encoding="utf-8")
                print(f"Exportado: {nombre_archivo} con {len(alumnos)} alumnos.")

    # Convalidaciones según el alumno
    def convalidaciones_alumno(self, entity: Student):
        # Como ya tenemos definida una propiedad en estudiante
        # que contiene una lista de convalidaciones, la devolvemos
        return entity.convalidations

    # Comprobación de si todas estan convalidadas
    def todas_convalidadas(self, entity: Student):
        # Cargamos las convalidaciones
        lista_convalidaciones: list[Convalidation] = entity.convalidations

        # Comprobamos que todas tengan el estado estimada
        todo_estimado = all(str(c.estado) == "estimada" for c in lista_convalidaciones)
        # Devolvemso el resultado, que será un booleano
        return todo_estimado
