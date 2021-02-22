from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self.amount_of_fabric = None

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 2)


suit_1 = Suit('пиджак отца', 1.85)
suit_2 = Suit('школьная форма брата', 1.20)
coat_1 = Coat('плащ Нео', 48)

print(f'{suit_1.name} - {suit_1.fabric_consumption}, '
      f'{suit_2.name} - {suit_2.fabric_consumption}, '
      f'{coat_1.name} - {coat_1.fabric_consumption}')
print(suit_1.fabric_consumption + suit_2.fabric_consumption + coat_1.fabric_consumption)
