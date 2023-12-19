from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def spell(self):
        ...

    def sing(self):
        print("I am not singing!!!")


class Warrior(Player):
    def fight(self):
        print("Swing a sword...")

    def spell(self):
        print("Heal wounds...")


warrior = Warrior("John", 1, 1)
warrior.fight()
warrior.spell()
warrior.sing()

# player = Player("ggg", 1, 1)
# player.fight()
