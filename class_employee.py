#statik method nemá nic společného s classsou ale kvůli celistvsoti es tam přidá, uplně basic fce, která se schová do té fce napr pracovni zakonik

class Employee: #zaciname vzdy velkym pismenem
    number_of_employees = 0
    #employer = 'Avast' #class promenna- taky atribut

    def __init__(self, name: str, surname: str, salary: int, active: bool): #atribut
        self.name = name
        self.surname = surname
        self.salary = salary
        self.active = active
        type(self).number_of_employees += 1  # = Employee.number_of_employees += 1

#     @classmethod
#     def change_employer(cls, new_employer: str) -> None:
#         cls.employer = new_employer

    @classmethod
    def get_number_of_employees(cls) -> int:
        return cls.number_of_employees

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

    def __repr__(self):
        return self.get_fullname()
        #diky tomu to pekne vytiskneme jeste je metora str, ktera se pouzije kdyt zavolame str(objekt)

    def __str__(self):
        return f"{self.name}"


# lukas = Employee('Lukas', 'Kucera', 10, True)
# print(lukas.get_fullname())
# print(lukas.get_salary())
# lukas.increase_salary_percentage(50)
# print(lukas.get_salary())
# lukas.fire_employee()
# print(lukas.get_salary())
# print(lukas.is_active())
# #print(Employee.get_fullname(self=lukas))
#
# pavla = Employee('Pavla', 'Hrabcova', 20, True)
# tomas = Employee('Tomas', 'Danek', 30, True)
