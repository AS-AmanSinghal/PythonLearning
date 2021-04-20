from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capatalizePetName(pets):
    return str(pets).upper()


print(list(map(capatalizePetName, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_number = [5, 4, 3, 2, 1]

numbers = sorted(my_number)
print(list(zip(numbers, my_strings)))

scores = [73, 20, 65, 19, 76, 100, 88]


def filterScores(item):
    return True if item > 50 else False


print(list(filter(filterScores, scores)))


def sumOfScoresAndNumbers(result, item):
    return result + item


myNumberResult = reduce(sumOfScoresAndNumbers, my_number, 0)

print(reduce(sumOfScoresAndNumbers, scores, myNumberResult))
