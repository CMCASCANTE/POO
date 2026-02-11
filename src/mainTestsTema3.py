from logic.logic import DataCleaner, DataLoader
from models.models import Student

# data = DataCleaner("ejemplo.xlsx")
# list_data = data.normalize()

# updata = DataLoader().upData(list_data)


stud = Student("11111111B")

print(stud.convalidations)

print("-" * 40)
for elm in stud.convalidations:
    print(elm.modulo)
