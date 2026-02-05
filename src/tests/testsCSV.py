from models.models import Student
from persistence.persistance import StudentDAO


class testsPersistence:

    def __init__(self):
        self.dao = StudentDAO()

    def testSelect(self):
        print(*"-" * 20)
        print("SELECT")
        print(*"-" * 20)
        alrdy_student = Student("S1")
        student = self.dao.select(alrdy_student)
        print(student.to_list())

    def testInsert(self):
        print(*"-" * 20)
        print("INSERT")
        print(*"-" * 20)
        new_student = Student("S5", "Juan Profesor", "M1;M3;M4")
        print(f"Insert = {self.dao.insert(new_student)}")
        list = self.dao.select_all()
        for t in list:
            print(t.to_list())

    def testUpdate(self):
        print(*"-" * 20)
        print("UPDATE")
        print(*"-" * 20)
        updated_student = Student("S5", "Juan Profesor Actualizado", "M2;M3")
        print(f"Update = {self.dao.update(updated_student)}")
        list = self.dao.select_all()
        for t in list:
            print(t.to_list())

    def testDelete(self):
        print(*"-" * 20)
        print("DELETE")
        print(*"-" * 20)
        updated_student = Student("S5", "Juan Profesor Actualizado", "M2;M3")
        print(f"Delete = {self.dao.delete(updated_student)}")
        list = self.dao.select_all()
        for t in list:
            print(t.to_list())
