class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Tom", 20)
cat2 = Cat("Jerry", 30)
cat3 = Cat("Rocky", 10)


def oldestCat(cat1, cat2, cat3):
    if cat1 < cat2 and cat1 < cat3:
        return cat1
    elif cat2 < cat3:
        return cat2
    else:
        return cat3


cat = oldestCat(cat1.age, cat2.age, cat3.age)
print(f"The Oldest cat is {cat} years old.")
