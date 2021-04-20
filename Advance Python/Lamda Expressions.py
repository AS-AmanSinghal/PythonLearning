from functools import reduce

my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda result, item: result + item, my_list, 0))
