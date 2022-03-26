# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    speed = 240
    color = "black"
    name = "Keonigsegg"
    is_police = False


    def __init__(self, name, speed, color, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    # Методы
    def on_start(self):
        return f"Go-go-go!!!"


    def on_stop(self):
        return f"STOP!!!"


    def turn(self, direction):
        return f"{self.turn} after 100 meters turn {direction} "


    def show_speed(self):
        return f"Your speed is {self.speed}"

class TownCar(Car):


    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        if self.speed > 60:
            print("Превышение скорости!!!")


class SportCar(Car):
    pass




class WorkCar(Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        if self.speed > 40:
            print("Превышение скорости!!!")



class PoliceCar(Car):
    pass




sample_car = Car(240, "black", "Kionigsegg", is_police=False)

town_car = TownCar('Isuzu', 60, 'orange', False)
print('1:\n' + town_car.on_start(), town_car.show_speed(), town_car.turn('left'), town_car.turn('right'), town_car.on_stop())

sport_car = SportCar('Kenigsegg', 360, 'grafit', False)
print('2:\n' + sport_car.on_start(), sport_car.show_speed(), sport_car.turn('left'), sport_car.on_stop())

work_car = WorkCar('MAN', 30, 'blue/white', False)
print('3:\n' + work_car.on_start(), work_car.show_speed(), work_car.turn('right'), work_car.on_stop())

police_car = PoliceCar('Ford', 180, 'black', True)
print('4:\n' + police_car.on_start(), police_car.show_speed(), police_car.turn('right'), police_car.on_stop())