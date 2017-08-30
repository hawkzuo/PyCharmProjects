# Functions are first-class objects, they can be:
# • assigned to a variable
# • an item in a list (or any collection)
# • passed as an argument to another function.


def circle_area(radius):
    return 3.14 * radius * radius


# default values are evaluated when function is defined
# Careful when passing into mutable parameters as default input
defaultInput = 10


def double_input(x=defaultInput):
    return x * 2


defaultInput = 20


# Passing by value
def swap(a, b):
    tmp = b
    b = a
    a = tmp


# */**
def variable_args(*args, **kwargs):
    """
    Simply print out the two types of arguments in any number of amount
    :param args: any number of positional arguments packed into a tuple
    :param kwargs: any number of keyword arguments packed into a dictionary
    :return: None
    """
    print(args)
    print(kwargs)


# Test bench
print(double_input())
a1 = 10
b1 = 1
swap(a1, b1)
print(a1)
print(b1)
variable_args('A', 'B', 'C', x=1, y=2, z=3, k=4)
va = variable_args
va('test', k=1, z=5)
