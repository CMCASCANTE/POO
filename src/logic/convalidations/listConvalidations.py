from persistence.persistance import Convalidation_DAO


# Clase que se encarga exclusivamente de gestionar la propiedad de la clase Student, que es la lista de convalidaciones.
# Se encarga de obtener la lista de convalidaciones a través del DAO y devolverla al estudiante
class ListConvalidations:

    def __init__(self):
        self.db_con = Convalidation_DAO()

    def lista_convalidations_student(self, Student):

        lista_convs = self.db_con.read_all({"dni": str(Student)})

        return lista_convs
