import random


class Employee: #zaciname vzdy velkym pismenem
    def __init__(self, name: str, surname: str, salary: int, active: bool):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.active = active


    def get_fullname(self) -> str:
        return self.name + ' ' + self.surname

    def fire_employee(self) -> None:
        self.salary = 0
        self.active = False

    def is_active(self) -> bool:
        return self.active

    def increase_salary_percentage(self, increase_salary: int):
        self.salary += (increase_salary/100)*self.salary

    def get_salary(self):
        return self.salary

lukas = Employee('Lukas', 'Kucera', 10, True)
print(lukas.get_fullname())
print(lukas.get_salary())
lukas.increase_salary_percentage(50)
print(lukas.get_salary())
lukas.fire_employee()
print(lukas.get_salary())
print(lukas.is_active())
#print(Employee.get_fullname(self=lukas))

pavla = Employee('Pavla', 'Hrabcova', 20, True)
tomas = Employee('Tomas', 'Danek', 30, True)

# trida team, byla by definovana zaměstnanci, bez konstrukturu, přidej zaměstnance do týmu add employee,
# třeba tým qa automation, zavolala bych metodu add employee a přidala bych tam všechny tři a poté metoda náhodně vyhodit jednoho z týmu
# když budu dělat třídu týmu, tak když tu třídu vyrobím, tak si ty lidi budu muset udržovat, takže v konstruktoru si předpřipravit prázdný list
#
class Team_of_employee:
    def __init__(self, name: str, surname: str):
        self.employee_list = []
        self.name = name
        self.surname = surname

    def get_fullname(self) -> str:
        return self.name + ' ' + self.surname

    def add_employee(self) -> list:
        self.employee_list.append(self.get_fullname())
        return self.employee_list

    def russioan_rulet(self) -> list:
        self.employee_list.pop(1)
        return self.employee_list

avla = Team_of_employee('Pavla', 'Hrabcova')
vla = Team_of_employee('Pav', 'Hrab')
print(avla.add_employee())
print(vla.add_employee())
#print(vla.russioan_rulet())



class Team_of_employee:
    def __init__(self, employee_name: list):
        self.employee_list = []
        self.employee_name = employee_name

    def add_employee(self) -> list:
        self.employee_list = self.employee_name
        return self.employee_list

    def russioan_rulet(self) -> list:
        random.shuffle(self.employee_list)
        self.employee_list.pop()
        return self.employee_list

selected_employees = ['Pavla Hrabcova', 'Tomas Danek', 'Lukas Kucera']
QA_team = Team_of_employee(selected_employees)
print(QA_team.add_employee())
print(QA_team.russioan_rulet())


#print(vla.russioan_rulet())

