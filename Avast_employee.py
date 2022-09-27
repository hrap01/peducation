from class_employee import Employee


class AvastEmployee(Employee):
    employer = 'Avast'

    def __str__(self):
        return f"{self.name} - '{type(self).employer}'"



#vyrobit obdobnou třídu northnon employee a obohatit to nějak a rozkošatet to
# ve smyslu dědičnostia zkusit přenastavování v poděděné clase i ve vlastní atd.
