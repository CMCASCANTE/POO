from .PresentationI import PresentationI
from persistence.persistance import Module_DAO, Cycle_DAO, Teacher_DAO, Student_DAO
from models.models import Cycle, Module, Student, Teacher
from .QuotaSingleton import QuotaSingleton


# Implementación de la lógica de la aplicación
class LogicMongo(PresentationI):

    def __init__(self):
        self.quota = QuotaSingleton()

    # Manejo de quota
    def get_quota(self):
        return self.quota.quota

    # Listar todos los ciclos
    def get_all_cycles(self) -> list:
        dao = Cycle_DAO()
        # Guardamos la lista
        list = dao.read_all()
        # Restamos el tamaño de la lista a la quota
        self.quota.check_quota(len(list))
        # Devolvemos la lista de todos los ciclos
        return list

    # Listar todos los módulos de un ciclo
    def get_modules_by_cycle(self, cycle: Cycle) -> list:
        dao = Module_DAO()
        # Cargamos todos los módulos y guardamos solo los que coincida con el ciclo
        module_list = [mod for mod in dao.read_all() if cycle == mod.cycle]
        # Restamos el tamaño de la lista a la quota
        self.quota.check_quota(len(module_list))
        # Devolvemos la lista
        return module_list

    # Obtener el profesor de un módulo
    def get_teacher_by_module(self, module: Module) -> Teacher:
        dao = Module_DAO()
        # Cargamos el módulo que coincida con el que estamos buscando
        module = dao.read(module)
        dao = Teacher_DAO()
        # Cargamos el profesor que coincida con el profesor del módulo si hay módulo
        teacher = dao.read(module.teacher) if module else None
        # Restamos 1 resultado de la quota
        self.quota.check_quota(1)
        # Devolvemos el profesor
        return teacher

    # Obtener estudiantes de 1 modulo
    def get_students_by_module(self, module: Module) -> list:
        dao = Student_DAO()
        # Listamos todos los alumnos y guardamos solo los que tengan el módulo
        lista_estudiantes = [stud for stud in dao.read_all() if module in stud.modules]
        # Restamos el tamaño de la lista a la quota
        self.quota.check_quota(len(lista_estudiantes))
        # Devolvemos la lista
        return lista_estudiantes

    # Obtener los módulos del alumno y a qué ciclo pertenecen
    def get_student_modules_and_cycle(self, student: Student) -> list:
        daoStud = Student_DAO()
        daoMod = Module_DAO()
        daoCy = Cycle_DAO()
        # Siendo algo mas compleja que las anteriores, primero comprobamos si el alumno existe
        # y si no devolvemos una lista vacía
        if not daoStud.read(student):
            self.quota.check_quota(1)
            return []
        # Guardamos todos los módulos del alumno que buscamos
        modules = [daoMod.read(mod) for mod in daoStud.read(student).modules]
        # Cargamos todos los ciclos de los modulos que hemos guardado
        cycles = [daoCy.read(mod.cycle) for mod in modules]
        # Recorremos todos los ciclos y añadimos a la lista de módulos comprobando
        # que no lo hayamos añadido ya
        for cycle in cycles:
            (
                modules.append(cycle)
                if not any(m._id == cycle._id for m in modules)
                else None
            )
        # Restamos el tamaño de la lista a la quota
        self.quota.check_quota(len(modules))
        # Devolvemos la lista de modulos a la que le hemos añadido tambien los ciclos
        return modules
