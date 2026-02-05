from .DAO import DAO
from models.models import Teacher


class TeacherDAO(DAO):
    def __init__(self):
        super().__init__("teachers", Teacher)
