from time import time


def myDecorator(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'{t2 - t1} time taken')

    return wrapper


@myDecorator
def longTime():
    print("1")
    for i in range(10000000):
        i * 5


@myDecorator
def longTime2():
    print("2")
    for i in list(range(10000000)):
        i * 5


longTime()
longTime2()


# Create Generator

def myGenerator(num):
    t1 = time()
    for i in range(num):
        yield i
    t2 = time()

    print(f'{t2 - t1} time taken')


for i in myGenerator(10000):
    pass
