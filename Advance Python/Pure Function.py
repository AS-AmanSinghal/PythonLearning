def multiple_by2(li):
    newList = []
    for items in li:
        newList.append(items * 2)
    return newList


print(multiple_by2([1, 2, 3, ]))


# map()

def multiplyFunction(items):
    return items * 2


print(list(map(multiplyFunction, [1, 2, 3])))


# filter()

def onlyOdd(item):
    return item % 2 != 0


print(list(filter(onlyOdd, [1, 2, 3, 4])))

# zip

my_list = [1, 2, 3]
your_list = [10, 20, 30]
another_list = [5, 6, 7]

print(list(zip(my_list, your_list)))
print(list(zip(my_list, your_list, another_list)))

# reduce()

from functools import reduce

my_list = [1, 2, 3]


def myFunction(acc, item):
    print(acc, item)
    return acc + item


print(reduce(myFunction, my_list, 0))
