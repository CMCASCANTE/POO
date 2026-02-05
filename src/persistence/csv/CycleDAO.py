from .DAO import DAO
from models.models import Cycle


class CycleDAO(DAO):
    def __init__(self):
        super().__init__("cycles", Cycle)
