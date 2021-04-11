def Highest_even(li):
    evenNumber = li[0]
    for i in li:
        if (i % 2 == 0) and (evenNumber < i):
            evenNumber = i
    return evenNumber


print(Highest_even([2, 10, 2, 3, 4, 8, 11]))
