from .PresentationI import PresentationI
from persistence.persistance import ModuleDAO, CycleDAO, TeacherDAO, StudentDAO
from models.models import Cycle, Module, Student, Teacher
from .QuotaSingleton import QuotaSingleton


# Implementación de la lógica de la aplicación
class LogicCSV(PresentationI):

    def __init__(self):
        self.quota = QuotaSingleton()

    # Manejo de quota
    def get_quota(self):
        return self.quota.quota

    # Listar todos los ciclos
    def get_all_cycles(self) -> list:
        dao = CycleDAO()
        # Guardamos la lista
        list = dao.select_all()
        # Restamos el tamaño de la lista a la quota
        self.quota.check_quota(len(list))
        # Devolvemos la lista de todos los ciclos
        return list

    # Listar todos los módulos de un ciclo
    def get_modules_by_cycle(self, cycle: Cycle) -> list:
        dao = ModuleDAO()
        # Cargamos todos los módulos y guardamos solo los que coincida con el ciclo
        module_list = [mod for mod in dao.select_all() if cycle == mod.cycle]
        # Restamos el tamaño de la lista a la quota
        self.quota.check_quota(len(module_list))
        # Devolvemos la lista
        return module_list

    # Obtener el profesor de un módulo
    def get_teacher_by_module(self, module: Module) -> Teacher:
        dao = ModuleDAO()
        # Cargamos el módulo que coincida con el que estamos buscando
        module = dao.select(module)
        dao = TeacherDAO()
        # Cargamos el profesor que coincida con el profesor del módulo
        teacher = dao.select(module.teacher)
        # Restamos 1 resultado de la quota
        self.quota.check_quota(1)
        # Devolvemos el profesor
        return teacher

    # Obtener estudiantes de 1 modulo
    def get_students_by_module(self, module: Module) -> list:
        dao = StudentDAO()
        # Listamos todos los alumnos y guardamos solo los que tengan el módulo
        lista_estudiantes = [
            stud for stud in dao.select_all() if module in stud.modules
        ]
        # Restamos el tamaño de la lista a la quota
        self.quota.check_quota(len(lista_estudiantes))
        # Devolvemos la lista
        return lista_estudiantes

    # Obtener los módulos del alumno y a qué ciclo pertenecen
    def get_student_modules_and_cycle(self, student: Student) -> list:
        daoStud = StudentDAO()
        daoMod = ModuleDAO()
        daoCy = CycleDAO()
        # Guardamos todos los módulos del alumno que buscamos
        modules = [daoMod.select(mod) for mod in daoStud.select(student).modules]
        # Cargamos todos los ciclos de los modulos que hemos guardado
        cycles = [daoCy.select(mod.cycle) for mod in modules]
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
