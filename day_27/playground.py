# # Unlimited Positional Arguments
#
# def add(*args):
#     sum = 0
#     # print(sum(args))
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(3, 4, 6, 7))
#
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)
#
#
#

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R", color="green")
print(my_car.make, my_car.model, my_car.color)


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
bar(1, 2)
