class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.is_going = False

    def attributes(self):
        return [self.speed, self.color, self.name, self.is_police]

    def go(self):
        if self.is_going:
            print(f'{self.color} {self.name} already in motion!')
        else:
            self.is_going = True
            print(f'{self.color} {self.name} is going')

    def stop(self):
        if not self.is_going:
            print(f'{self.color} {self.name} already stopped!')
        else:
            self.is_going = False
            print(f'{self.color} {self.name} has stopped')

    def turn(self, direction):
        print(f'{self.color} {self.name} turn {direction}')

    def show_speed(self):
        if self.is_going:
            print(f'{self.color} {self.name} is going with speed {self.speed}')
        else:
            print(f'{self.color} {self.name} is standing still. Speed = 0')


class TownCar(Car):

    def show_speed(self):
        if self.is_going:
            print(f'{self.color} {self.name} is going with speed {self.speed}')
            if self.speed > 60:
                print(f'{self.color} {self.name} have exceeded the speed limit!')
        else:
            print(f'{self.color} {self.name} is standing still. Speed = 0')


class WorkCar(Car):

    def show_speed(self):
        if self.is_going:
            print(f'{self.color} {self.name} is going with speed {self.speed}')
            if self.speed > 40:
                print(f'{self.color} {self.name} have exceeded the speed limit!')
        else:
            print(f'{self.color} {self.name} is standing still. Speed = 0')


car_1 = TownCar(70, 'white', 'Toyota', False)
print(car_1.speed, car_1.color, car_1.name)
car_2 = Car(35, 'red', 'Nissan', False)
print(car_2.speed, car_2.color, car_2.name)
car_3 = Car(120, 'white-blue', 'Land Rover', True)
print(car_3.speed, car_3.color, car_3.name)
car_4 = WorkCar(45, 'green', 'UAZ', False)
print(car_4.speed, car_4.color, car_4.name)
car_5 = WorkCar(30, 'yellow', 'Volga', False)
print(car_5.speed, car_5.color, car_5.name)

car_1.go()
car_1.turn('left')
car_1.show_speed()
car_1.stop()
car_1.stop()

car_2.go()
car_2.turn('right')
car_2.show_speed()
car_2.stop()
car_2.stop()

car_3.go()
car_3.turn('right')
car_3.show_speed()
car_3.stop()

car_4.go()
car_5.go()
car_4.turn('right')
car_4.turn('left')
car_4.show_speed()
car_5.stop()
car_5.show_speed()
car_4.show_speed()
car_4.stop()
