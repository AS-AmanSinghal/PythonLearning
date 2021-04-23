def specialFor(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


specialFor([1, 2, 3, 4, 5])


class MyGenerator():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration


myGen1 = MyGenerator(0, 100)

for i in myGen1:
    print(i)
