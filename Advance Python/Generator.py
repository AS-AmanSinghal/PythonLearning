# Generator


def generator_function(num):
    for i in range(num):
        yield i * 2


# for item in generator_function(1000):
#     print(item)

g = generator_function(1000)
print(g)  # return generator memory location
print(next(g))  # get next value -> 0
print(next(g))  # get next value ->2
