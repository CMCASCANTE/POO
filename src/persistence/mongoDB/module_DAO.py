from .DAO import DAO
from models.models import Module


class Module_DAO(DAO):
    def __init__(self):
        super().__init__("modules", Module)
