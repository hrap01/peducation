from class_employee import Employee
from typing import ClassVar, List, Dict, Any

# A -> B -> C

class AvastEmployee(Employee):
    employer: ClassVar[str] = 'Avast'
    message_tool: str = 'Slack'
    l: List[str] = []
    d: Dict[str, Any] = {}

    def __init__(self, name: str, surname: str, salary: int, active: bool):
        super(AvastEmployee, self).__init__(name, surname, salary, active)

    @classmethod
    def change_employer_to_northon(cls) -> None:
        cls.employer = 'Northon'

    def __str__(self) -> str:
        return f"{self.name} - '{type(self).employer}'"

Vendula = AvastEmployee('Vendula', 'Hrabcova', 10, True)
print(Vendula)
print(Vendula.increase_salary_percentage(50))
print(Vendula.get_number_of_employees())
print(Vendula.change_employer_to_northon())
print(Vendula)
Vendula.fire_employee()
print(Vendula.active)


#vyrobit obdobnou třídu northnon employee a obohatit to nějak a rozkošatet to
# ve smyslu dědičnostia zkusit přenastavování v poděděné clase i ve vlastní atd.

# geometrické tvary nebo zvířátka a nastavit si to
