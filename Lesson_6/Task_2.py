class Road:

    __asphalt_mass_per_m2 = 20

    def __init__(self, length, wide):
        self._length = length
        self._wide = wide

    def mass(self, thickness):
        return self._length * self._wide * Road.__asphalt_mass_per_m2 * thickness


test_road_1 = Road(200, 10)
print(test_road_1.mass(4))

test_road_2 = Road(10, 10)
print(test_road_2.mass(10))

print(test_road_1.mass(100))

