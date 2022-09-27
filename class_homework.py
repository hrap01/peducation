#jak budeme konstruovat obět - prázdný list a add emplyee a nebo možnost 2, že ten tým vytvoříme tak, že to rovnou naplníme členy

import random
from class_employee import Employee
from typing import List


class TeamOfEmployee:
    def __init__(self, employee_object_list: List[Employee]):
        self.employee_object_list = employee_object_list

    def get_list_of_employees(self) -> List[Employee]:
        return self.employee_object_list

    def add_another_employee(self, another_employee: Employee):
        self.employee_object_list.append(another_employee)

    def russian_roulette(self) -> List[Employee]:
        random_number = random.randint(0, len(self.employee_object_list) - 1)
        redundant_employee_list = [self.employee_object_list.pop(random_number)]
        return redundant_employee_list

#class_employee namespace
lukas = Employee('Lukas', 'Kucera', 10, True)
pavla = Employee('Pavla', 'Hrabcova', 20, True)
tomas = Employee('Tomas', 'Danek', 30, True)

#podivat se kdy se zavola repr a kdy str
selected_employees = [lukas, pavla, tomas]
#print(selected_employees)
#print(lukas)
# ['Pavla Hrabcova', 'Tomas Danek', 'Lukas Kucera']
qa_team = TeamOfEmployee(selected_employees)
qa_team.add_another_employee(Employee('Pepa', 'Vodvarka', 31, True))
print(qa_team.get_list_of_employees())
print(qa_team.russian_roulette())
print(qa_team.get_list_of_employees())
print(Employee.number_of_employees)

