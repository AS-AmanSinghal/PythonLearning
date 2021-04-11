def Checker(age):
    if age < 18:
        return "Sorry,you are too young to drive this car.Powering off"
    elif age == 18:
        return "Congratulations on your first year of driving. Enjoy the ride!"
    else:
        return "Powering On. Enjoy the ride."


print(Checker(17))
print(Checker(18))
print(Checker(19))
print(Checker(55))
