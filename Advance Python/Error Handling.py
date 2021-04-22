# Error Handling
# 1
try:
    age = int(input("What is your Age? \n"))
    print(age)
except:
    print("Please Enter Number")

# 2
while True:
    try:
        age = int(input("What is your Age? \n"))
        print(age)
    except (ValueError, ZeroDivisionError)as err:
        print(f"Please Enter Number {err}")
    else:
        print("Thank You")
        break
