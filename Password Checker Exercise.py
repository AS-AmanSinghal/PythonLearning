username = input("Enter your Username \n")
password = input("Enter your Password \n")

passwordLength = len(password)
password = '*' * passwordLength
print(f'Hi {username}, your {password} is {passwordLength} letter long')
