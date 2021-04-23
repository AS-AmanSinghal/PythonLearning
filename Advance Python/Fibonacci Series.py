def fibonacciGenerator(num):
    num1 = 0
    num2 = 1
    for i in range(num):
        yield num1
        temp = num1
        num1 = num2
        num2 += temp


for i in fibonacciGenerator(21):
    print(i)
