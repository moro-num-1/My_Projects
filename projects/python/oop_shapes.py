#super() = Function used in a child class to call methods from a parent class (superclass);
#          Allow you to extend functionality of the inherit methods;

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)        
        self.radius = radius

class Square(Shape):
    def __init__(self, width, color, filled):
        Shape.__init__(self, color, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        Shape.__init__(self, color, filled)
        self.width = width
        self.height = height

triangle = Triangle(color="Blue", filled=True, width=7, height=8)
print(f"Triangle is: {triangle.color}, {"Empty" if not triangle.filled else "Filled"}, {triangle.width}cm, {triangle.height}cm")