from models.models import Student
from persistence.persistance import Student_DAO
from .insertTestData import insert_test_data


class testsPersistence:

    def __init__(self):
        self.dao = Student_DAO()

    def init_test_data(self):
        insert_test_data()

    def testRead(self):
        print(*"-" * 20)
        print("read")
        print(*"-" * 20)
        alrdy_student = Student("1")
        student = self.dao.read(alrdy_student)
        print(student.to_list())

    def testInsert(self):
        print(*"-" * 20)
        print("INSERT")
        print(*"-" * 20)
        new_student = Student("5", "Juan Profesor", "1;3;4")
        print(f"Insert = {self.dao.insert(new_student)}")
        list = self.dao.read_all()
        for t in list:
            print(t.to_list())

    def testUpdate(self):
        print(*"-" * 20)
        print("UPDATE")
        print(*"-" * 20)
        updated_student = Student("5", "Juan Profesor Actualizado", "2;3")
        print(f"Update = {self.dao.update(updated_student)}")
        list = self.dao.read_all()
        for t in list:
            print(t.to_list())

    def testDelete(self):
        print(*"-" * 20)
        print("DELETE")
        print(*"-" * 20)
        updated_student = Student("5", "Juan Profesor Actualizado", "2;3")
        print(f"Delete = {self.dao.delete(updated_student)}")
        list = self.dao.read_all()
        for t in list:
            print(t.to_list())
