from class_employee import Employee


class AvastEmployee(Employee):
    employer = 'Avast'
    message_tool = 'Slack'

    @classmethod
    def change_employer_to_northon(cls):
        cls.employer = 'Northon'

    def __str__(self):
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
