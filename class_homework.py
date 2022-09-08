#jak budeme konstruovat obět - prázdný list a add emplyee a nebo možnost 2, že ten tým vytvoříme tak, že to rovnou naplníme členy

import random


class Team_of_employee:
    def __init__(self, employee_name_list: list):
        self.employee_name_list = employee_name_list

    def get_list_of_employees(self) -> list:
        return self.employee_name_list

    def add_another_employee(self, another_employee):
        self.employee_name_list.append(another_employee)

    def russian_roulette(self) -> list:
        random_number = random.randint(0, len(self.employee_name_list)-1)
        redundant_employee_list = [self.employee_name_list.pop(random_number)]
        return redundant_employee_list


selected_employees = ['Pavla Hrabcova', 'Tomas Danek', 'Lukas Kucera']
QA_team = Team_of_employee(selected_employees)
QA_team.add_another_employee('Pepa Vodvarka')
print(QA_team.get_list_of_employees())
print(QA_team.russian_roulette())
print(QA_team.get_list_of_employees())
