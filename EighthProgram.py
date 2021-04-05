# check for input is greater than 18 or not.

isChecker = False

a = int(input("Please Enter your Age...\n"))

if a >= 18:
    isChecker = True

if isChecker:
    print("You can drive your Car")
else:
    print("You are not eligible for Car")
