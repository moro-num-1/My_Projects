#Show what the actual inheritance look like;

class Parent:
    def __init__(self, x):
        self.x = x
    def f1():
        print("You're calling the first function")
    def f2():
        print("You're calling the second function")
    
    def f3():
        print("You're calling the third function")
    
class Child(Parent):
    def __init__(self):
        Child.f1()
        Child.f2()
        Child.f3()
print(dir(Parent))
print(dir(Child))
Child()