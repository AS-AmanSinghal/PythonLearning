import random

while True:
    try:
        number = int(input("Guess the Number from 1 to 10?"))

        if number == random.randint(1,10):
            print("Genius")
            break
        else:
            print("Opps Try Again\n")
    except:
        print('Please Enter Number only')