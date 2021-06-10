class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_income(self):
        return self._income['wage'] + self._income['bonus']


pos = Position("Марк", "Иванов", "Программист", "123.6654", "78331")

print(pos.get_full_name())
print(pos.get_full_income())
