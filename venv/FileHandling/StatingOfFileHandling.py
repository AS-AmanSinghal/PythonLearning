myfile = open('test.txt')
# print(myfile.read())
# myfile.seek(0)
# print(myfile.read())
# myfile.seek(2)   # it is used for set the cursor position
# print(myfile.read()) #used to read file

# print(myfile.readline()) # it is used to read line one by one

print(myfile.readlines())  #it is used to read all the lines of file and return them in the form of list.

myfile.close()