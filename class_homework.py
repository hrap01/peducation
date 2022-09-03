import random


class Team_of_employee:
    def __init__(self, employee_name: list):
        self.employee_list = []
        self.employee_name = employee_name

    def add_employee(self) -> list:
        self.employee_list = self.employee_name
        return self.employee_list

    def russian_roulette(self) -> list:
        random.shuffle(self.employee_list)
        self.employee_list.pop()
        return self.employee_list


selected_employees = ['Pavla Hrabcova', 'Tomas Danek', 'Lukas Kucera']

QA_team = Team_of_employee(selected_employees)
print(QA_team.add_employee())
print(QA_team.russian_roulette())
