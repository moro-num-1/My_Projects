#"Duck Typing" = Another way to achieve Polymorphism besides Inheritance;
#                Object must have the minimum necessary attributes/methods
#                "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True
    def __init__(self, name):
        self.name = name

    if not alive:
        def die(self):
            print(f"{self.name} is dead")

class Cat(Animal):
    if Animal.alive:
        def speak(self):
            print("Meow")


class Dog(Animal):
    if Animal.alive:
        def speak(self):
            print("Wolf")

class Car:
    def speak(self):
        print("Honk")

animals = [Cat(name="Kitten"), Dog(name="Rox"), Car()]

for animal in animals:
    animal.speak()