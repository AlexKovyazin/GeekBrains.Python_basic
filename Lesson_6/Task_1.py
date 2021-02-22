import time


class TrafficLight:
    __color = None
    types_of_colors = ['red', 'yellow', 'green']

    def running(self, num_of_cycles):
        for i in range(num_of_cycles):
            for color in TrafficLight.types_of_colors:
                TrafficLight.__color = color
                if TrafficLight.__color == 'red':
                    print(f'\033[031m {TrafficLight.__color}')
                    time.sleep(7)
                elif TrafficLight.__color == 'yellow':
                    print(f'\033[033m {TrafficLight.__color}')
                    time.sleep(2)
                elif TrafficLight.__color == 'green':
                    print(f'\033[032m {TrafficLight.__color}')
                    time.sleep(4)


test = TrafficLight()
test.running(2)
