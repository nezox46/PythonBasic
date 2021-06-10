class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = str(name)
        self.speed = int(speed)
        self.color = color
        self.is_police = bool(is_police)

    @property
    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость машины {self.name} - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превышаете - {self.speed}, пожалуйста, снизьте скорость'
        else:
            return f'Молодец, вы не превышаете, Ваша скорость - {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превышаете - {self.speed}, пожалуйста, снизьте скорость'
        else:
            return f'Молодец, Вы не превышаете, Ваша скорость - {self.speed}'


class PoliceCar(Car):
    pass


town = TownCar('BMW', 70, 'Черный', False)
print(town.go, town.show_speed(), town.turn('направо'), town.stop())

sport = SportCar('Chevrolet', 210, 'Желтый', False)
print(sport.go, sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('Камаз', 20, 'Серый', False)
print(work.go, work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Toyota', 123, 'Синий', True)
print(police.go, police.show_speed(), police.turn('налево'), police.turn('направо'), police.stop())
