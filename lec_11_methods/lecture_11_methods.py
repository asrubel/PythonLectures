class Ship:
    num = 0

    def __new__(cls, *args, **kwargs):
        cls.num += 1
        print("New ship")
        return object.__new__(cls)

    def __init__(self, name, capacity):
        print("Ship initialized")
        self.captain = None
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def name_captain(self, captain):
        self.captain = captain
        print(f"New captain assigned to this ship: {self.captain}!")

    def sail(self):
        print(f"{self.name} is sailing...")

    def convert_to_kg(self):
        return self.capacity * 1000

    def load_cargo(self, weight):
        if weight + self.cargo > self.capacity:
            print(f"Loading {weight} tons. Cannot do that!")
        else:
            self.cargo += weight
            print(f"Loading {weight} tons. Done!")

    def unload_cargo(self, weight):
        if self.cargo - weight < 0:
            print(f"Unloading {weight} tons. Cannot do that!")
        else:
            self.cargo -= weight
            print(f"Unloading {weight} tons. Done!")

    def show_declaration(self):
        print(f"{self.name}.\nCaptain: {self.captain}.\nCargo: {self.cargo} tons.")

    def __str__(self):
        return f"Ship {self.name} with captain {self.captain}"

    def __add__(self, other):
        self.load_cargo(other)
        return self

    def __sub__(self, other):
        self.unload_cargo(other)
        return self

    def __iadd__(self, other):
        self.load_cargo(other)
        return self

    def __isub__(self, other):
        self.unload_cargo(other)
        return self


def sail_fun(name):
    print(f"{name} is sailing...")


# Instantiate objects of class Ship
ship = Ship("Black Pearl", 100)
ship_2 = Ship("Titanic", 10000)

# Checking simple methods
ship.sail()
ship_2.sail()
print(ship.convert_to_kg(), "kg")

# Checking methods working with properties
ship.load_cargo(50)
ship.show_declaration()
ship.load_cargo(100)
ship.show_declaration()
ship.load_cargo(50)
ship.show_declaration()

ship.unload_cargo(75)
ship.show_declaration()
ship.unload_cargo(75)
ship.show_declaration()

# Check dynamic properties - NOT GOOD
ship.name_captain("Jack Sparrow")
print(ship.captain)
print(ship_2.captain)

# Check math magic methods
ship = ship + 50
ship += 50
ship.show_declaration()
ship = ship - 50
ship -= 50
ship.show_declaration()

# Check __str__ magic method
print(ship)
