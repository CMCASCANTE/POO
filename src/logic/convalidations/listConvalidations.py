from persistence.persistance import Convalidation_DAO


class ListConvalidations:

    def __init__(self):
        self.db_con = Convalidation_DAO()

    def lista_convalidations_student(self, Student):

        lista_convs = self.db_con.read_all({"dni": str(Student)})

        return lista_convs
