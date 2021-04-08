for i, data in enumerate(list(range(100))):
    if i == 50:
        print(data)

pictures = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for list in pictures:
    for li in list:
        if li == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print("\n")

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for list in some_list:
    if some_list.count(list) > 1:
        if list not in duplicates:
            duplicates.append(list)

print(duplicates)
