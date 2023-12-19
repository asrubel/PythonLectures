class MyClass:
    ...


class AnotherClass(object):
    ...


print(dir(MyClass))


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    ...


cat = Animal("Fluffy")
dog = Dog("Reks")

print(type(cat))
print(type(dog))

print(isinstance(cat, Animal))
print(isinstance(cat, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
