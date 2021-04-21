# Decorator

def myDecorator(func):
    def wrapFunc():
        print("**************")
        func()
        print("***********")

    return wrapFunc


@myDecorator
def hello():
    print("Helllo")


@myDecorator
def bye():
    print("See You Later")


hello()
bye()


def myDecorator2(func):
    def wrapFunc(param):
        print("**************")
        func(param)
        print("***********")

    return wrapFunc


@myDecorator2
def gretting(greet):
    print(greet)


gretting("AMAN")


# Decorator Pattern

def myDecorator3(func):
    def wrapFunction(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")

    return wrapFunction


@myDecorator3
def hello(greeting, emoij=":("):
    print(greeting, emoij)


hello("Hello PAGAL", emoij="):")
