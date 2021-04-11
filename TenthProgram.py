def Hello():
    print("Hello World")


Hello()


# positional parameter
def PositionalParameterFunction(name, age):
    print(f'Hello {name}. Your age is {age}')


# positional argument   (In this type of function position matters)
PositionalParameterFunction('AMAN', '23')

# keyword argument

PositionalParameterFunction(age='23', name='AMAN')


# default parameter

def fun(name='Aman', age='13'):
    print(f'Hello {name}. Your age is {age}')


fun()
fun("Rohit")
fun("Rohit", "24")

# def sum(num1, num2):
#     return num1 + num2


# print(sum(3, 4))

# methods

print('hello aman'.capitalize())


# functions

def some():
    print("Hello")


# *args and **kwargs

def super_function(*args):
    print(args)
    return sum(args)


print(super_function(1, 2, 3, 4, 5))


def super(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    print(total)


super(1, 2, 3, 4, num=23, num1=23)

# Walrus Operator

a = "Helloooooooooooooooooooo"

if ((n := len(a)) > 10):
    print(f"Too much character i.e. {n}")
