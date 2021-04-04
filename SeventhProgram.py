# tuple
# It is just like list but they are immutable.

my_tuple = (1, 2, 3, 4, 5, 6)

print(my_tuple.count(3))
print(my_tuple.index(3))

# set
# it is a simple unordered collections of unique objects
# it has unique value

my_set = {1, 2, 3, 4, 5}
my_set1 = {1, 2, 3, 4, 5, 5, 2}
print(my_set)
print(my_set1)

my_set.add(100)
my_set.add(2)
print(my_set)

# type conversion

my_list = [1, 2, 3, 3, 4, 5, 5, 6, 6]

my_set2 = set(my_list)
print(my_set2)
