# Decorator = A function that extends the behavior of another function
#             W/O modifying the base function
#             Pass the base function as an argument to the decorator

def add_sprinkles(func):
        print("*You add sprinkles🍨*")
        def wrapper():
            func()
        return wrapper

def add_fudge(func):
    print("*You add fudge 🍫*")
    def wrapper():
        func()
    return wrapper()

@add_fudge
@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream🍦")