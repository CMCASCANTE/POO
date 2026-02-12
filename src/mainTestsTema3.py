from logic.logic import DataCleaner, upData
from models.models import Student

data = DataCleaner("ejemplo.xlsx")
upData(data.normalize())

stud = Student("11111111B")

stud.set_convalidations()

print(stud.convalidations)

print("-" * 40)
for elm in stud.convalidations:
    print(elm.ciclo)
