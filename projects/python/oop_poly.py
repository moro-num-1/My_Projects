#Polymorphism = Greek word that means to "have many forms or faces";
#               Poly = Many;
#               Morph = Form;
#Tow ways to achieve Polymorphism;
#               1.Inheritance = An object could be treated of the same type as a parent class;
#               2."Duck Typing" = An object must have necessary attributes/methods; 

#Classes;

from abc import abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return self.height * (self.base * 0.5)

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

#Objects;
shapes = (Circle(4), Square(5), Triangle(6, 7), Pizza("Eggs", 15))

for shape in shapes:
    print(f"{shape.area()}²")