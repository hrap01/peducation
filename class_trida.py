#předpis = class = třída a instance je samotná aplikace a tech může být nekonečno
# list je classa/předpis seznamu
#metoda fce spojena s class
#každá třída má konstruktor a destruktor
#program leakuje - vytvořím proměnou, alokuju pamět, uložím ji do paměti, pracují si, fce zmizí, ale ta pamět zustava naalokovaná
# python má garbage kolektor, dělá to a zkoumá objejty co tam jsou, jsou tam reference count, kolikrát na to kdo vidí a má ho uložené v paměti a v momentě kdy je reference count na nule tak ho vyhodí
#gargbahe kolektor ao bíhá objekty a dívá se na reference count
#objekt si drzi atributy

class employee:

    def __init__(self, name, salary): #konstruktor
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

lukas = employee('lukas', 1)

print(lukas.name)

