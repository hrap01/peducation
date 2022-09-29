from class_employee import Employee


class NorthonEmployee(Employee):
    employer = 'Northon'
    message_tool = 'MS Teams'
    country = 'India'

    @classmethod
    def country_of_origin(cls, country):
        cls.country = country

    def __str__(self):
        return f"{self.name} - '{type(self).employer}'"

Ludmila = NorthonEmployee('Ludmila', 'Hrabcova', 20, True)
print(Ludmila)
Ludmila.country_of_origin('Czechia')
print(Ludmila.country)