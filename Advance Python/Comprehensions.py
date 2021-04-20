# list Comprehensions

myList = [char for char in 'Hello']
print(myList)

print([number for number in range(0, 101)])
myList2 = [num ** 2 for num in range(0, 101)]
print(myList2)
print([myList for myList in myList2 if myList % 2 == 0])

# Set Comprehensions

myList = {char for char in 'Hello'}
print(myList)

print({number for number in range(0, 101)})
myList2 = {num ** 2 for num in range(0, 101)}
print(myList2)
print({myList for myList in myList2 if myList % 2 == 0})

# Dictionary Comprehensive

simpleDictionary = {
    'a': 1,
    'b': 2
}

my_dict = {key: value ** 2 for key, value in simpleDictionary.items()}
print(my_dict)

my_dict1 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict1)
