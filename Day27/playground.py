def add(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


def calculate(n,**kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw) -> None:
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')

car = Car()
print(car.colour)