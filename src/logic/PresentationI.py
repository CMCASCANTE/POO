# Interfaz para la presentación de la aplicación
class PresentationI:

    def get_all_cycles(self):
        """Devuelve todos los ciclos"""
        raise NotImplementedError()

    def get_modules_by_cycle(self, cycle):
        """Filtra módulos por el ID del ciclo"""
        raise NotImplementedError()

    def get_teacher_by_module(self, module):
        """Busca el Teacher asignado a un módulo"""
        raise NotImplementedError()

    def get_students_by_module(self, module):
        """Lista alumnos cuya lista 'module_ids' contenga el ID buscado"""
        raise NotImplementedError()

    def get_student_modules_and_cycle(self, student):
        """Devuelve los módulos del alumno y a qué ciclo pertenecen"""
        raise NotImplementedError()

    def is_teacher_own_student(self, teacher):
        """Comprueba si el ID de profesor existe en la lista de alumnos"""
        raise NotImplementedError()
