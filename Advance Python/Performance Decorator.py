from time import time


def performance(func):
    def wrapFunction(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"take {t1} and {t2} and difference is {t2 - t1} seconds ")
        return result

    return wrapFunction


@performance
def long_time():
    for i in range(1000000000):
        pass


long_time()
