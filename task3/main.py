'''
Класс «Автобус». Класс содержит свойства:
● скорость
● максимальное количество посадочных мест
● максимальная скорость
● список фамилий пассажиров
● флаг наличия свободных мест
● словарь мест в автобусе
Методы:
● посадка и высадка одного или нескольких пассажиров
● увеличение и уменьшение скорости на заданное значение
● операции in, += и -= (посадка и высадка пассажира по
фамилии)
'''
class Bus:
    def __init__(self, speed, max_seats, max_speed):
        self.speed = speed
        self.max_speed = max_speed
        self.max_seats = max_seats
        self.passengers = []
        self.free_seats = True
        self.seats = {}
        self.free_seats_count = max_seats
    def land_passengers(self, *passengers):
        if len(self.passengers) + len(passengers) <= self.max_seats and self.free_seats_count >= len(passengers):
            for passenger in passengers:
                self.passengers.append(passenger)
                self.seats[passenger] = len(self.passengers)
                self.free_seats_count -= 1
        else:
            return f"Нету свободных мест"

    def kick_out_passengers(self, *passengers):
        for passenger in passengers:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                del self.seats[passenger]
                self.free_seats_count += 1
            else:
                print(f"{passenger} нету в списке пассажиров")


    def increase_speed(self, value):
        self.speed += value

    def decrease_speed(self, value):
        self.speed -= value

    def __contains__(self, item):
        return item in self.passengers

    def __iadd__(self, passenger):
        if isinstance(passenger, str):
            self.land_passengers(passenger)
            return self
        else:
            return f"Фамилия пассажира должна быть строковым типом"

    def __isub__(self, passenger):
        if isinstance(passenger, str):
            self.kick_out_passengers(passenger)
            return self
        else:
            return f"Фамилия пассажира должна быть строковым типом"

    def __str__(self):
        return f"Текущая скорость {self.speed}, список пассажиров {self.passengers}, словарь мест {self.seats}"

bus = Bus(100, 30, 250)
bus.land_passengers("Артем", "Настя", "Андрей", "Катя", "Никита", "Руслан")
print(str(bus))
bus += "Слава"
print(str(bus))
bus -= "Никита"
print(str(bus))
check_name = "Катя"
print(check_name in bus)
check_name2 = "Вика"
print(check_name2 in bus)
bus.increase_speed(34)
print(str(bus))