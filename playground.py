def add(*args):
    total = 0
    for i in args:
        total += i
    return total


# print(add(5, 8, 9, 2, 4, 7))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GT-R")

class Car2:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car2 = Car2(make="Nissan")

print(my_car2.model)
