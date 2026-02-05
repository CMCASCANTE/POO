from .DAO import DAO
from models.models import Student


class StudentDAO(DAO):
    def __init__(self):
        super().__init__("students", Student)
