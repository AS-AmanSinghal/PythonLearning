isMagician = True

isExpert = False

if isMagician and isExpert:
    print("You are a master magician")
elif isMagician and not (isExpert):
    print("At least you're getting there")
elif not (isMagician):
    print("You need a magic power")

# exercise two - - -> Tricky Counter

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0

for item in myList:
    count += item
print(count)
