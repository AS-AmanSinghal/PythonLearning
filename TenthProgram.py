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


def sum(num1, num2):
    return num1 + num2


print(sum(3, 4))

# methods

print('hello aman'.capitalize())


# functions

def some():
    print("Hello")


some()
