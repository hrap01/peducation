from class_employee import Employee


class NorthonEmployee(Employee):
    employer = 'Northon'

    def __str__(self):
        return f"{self.name} - '{type(self).employer}'"

