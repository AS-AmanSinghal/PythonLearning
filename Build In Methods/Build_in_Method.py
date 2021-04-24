import random

# print(random)
#
# help(random)  #which provide documentation and help with respective argument pass.
#
#
# print(dir(random))  #shows the methods available in this class or argument.

print(random.randint(1, 6))
print(random.choice([1, 2, 3, 4, 5]))
myList = [1, 2, 3, 4, 5]

print(random.shuffle(myList))
print(myList)
