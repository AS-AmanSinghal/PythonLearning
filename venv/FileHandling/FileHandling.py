# with open('test.txt',mode='r+') as myFile:
#     text = myFile.write("hey bndr kesa hai")
#     print(text) #count

    # print(myFile.readline())
    # myFile.seek(0)
    # print(myFile.readlines())


# with open('test.txt',mode='a') as myFile:
#     text = myFile.write("AMAN")
#     print(text)
try:
    with open('happsdsy.txt',mode='r') as myFile:
        myFile.write("Kya ho rha bachcha?")
except FileNotFoundError:
    print("File not Found")