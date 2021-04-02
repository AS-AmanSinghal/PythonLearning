# list
# It is called as sequence of objects

li = [1, 2, 3, 4, 5]
li1 = ['a', 'b', 'c']

li2 = [1, 2, 3, 'a', 'b', 2.4, True]

print(li2[2])

# list slicing

print(li2[0:2])

li2[2] = 4

print(li2)

# matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])

# list functions

basket = [1, 2, 3, 4, 5]

print(len(basket))

# adding methods
print(basket.append(10))
print(basket)

basket.insert(4, 100)
print(basket)

basket.extend([1, 2, 3, 4, 5, 6])
print(basket)

# removing methods

print(basket.pop())
print(basket)

print(basket.pop(2))
print(basket)

print(basket.remove(5))
print(basket)

print(basket.remove(4))
print(basket)

# print(basket.clear())
# print(basket)

# index

print(basket.index(2))

print(2 in basket)

print(basket.count(4))

# sort

print(basket.sort())
print(basket)

print(sorted(basket))

# range
li3 = []
for i in range(1, 50):
    li3.append(i)
print(li3)

# join

sentence = ''
print(sentence.join(['hi', 'my', 'name', 'is', 'AMAN']))
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'AMAN'])
print(new_sentence)

# list unpacking

unpacking = [1, 2, 3]
a, b, c = unpacking

print(a)
print(b)
print(c)

basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a, b, c, *other, d = basket
print(a)
print(b)
print(c)
print(other)
print(d)
