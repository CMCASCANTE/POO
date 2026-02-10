from persistence.persistance import DAO


class ListConvalidations:

    def __init__(self):
        self.db_con = DAO()

    def lista_convalidations_student(self, Student):
        # l = [self.db_con.read_all()]
        # print(l)
        lista_convs = self.db_con.read_all({"dni": str(Student)})
        return lista_convs
