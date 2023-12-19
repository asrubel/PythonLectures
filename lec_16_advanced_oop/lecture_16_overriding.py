class ParentClass:
    def __init__(self, name):
        self.name = name
        print("Parent __init__()")

    def do_smt(self):
        print("Do something...")


class ChildClass(ParentClass):
    def __init__(self, name):
        super().__init__(name)
        print("Child __init__()")

    def do_smt(self):
        print("Do something else...")


parent = ParentClass("John")
child = ChildClass("Jack")

parent.do_smt()
child.do_smt()


class Car:
    def __init__(self, number):
        self.number = number

    def move(self):
        print(f"Car [{self.number}] is moving...")

    def carry(self, cargo):
        print(f"Car [{self.number}] is carrying {cargo}")


class Tractor(Car):
    def carry(self, cargo):
        print(f"Tractor is carrying cargo: {cargo}")


class Ambulance(Car):
    def carry(self, cargo):
        super().carry(cargo)
        print(f"Siren is wheeling!!!!")


class Auto(Car):
    def __init__(self, number, body):
        super().__init__(number)
        self.body = body

    def move(self):
        print(f"Car ({self.body}) is moving...")


auto = Auto("XA123456", "sedan")
ambulance = Ambulance("XA556788")
tractor = Tractor("XA789000")

auto.move()
ambulance.move()
tractor.move()

auto.carry("4 passengers")
ambulance.carry("1 patient")
tractor.carry("10 tons of rubbish")
