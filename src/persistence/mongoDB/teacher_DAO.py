from .DAO import DAO
from models.models import Teacher


class Teacher_DAO(DAO):
    def __init__(self):
        super().__init__("teachers", Teacher)
