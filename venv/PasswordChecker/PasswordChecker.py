import hashlib

import requests

def requestApiData(queryCharacter):
    url = "https://api.pwnedpasswords.com/range/"+queryCharacter
    res = requests.get(url)
    if res.status_code == 200:
        return res
    else:
        raise RuntimeError(f'Error Fetching {res.status_code}')


def getPasswordLeaksCount(hashes,password):
    hashes = (line.split(':') for line in hashes.splitlines())
    for h,count in hashes:
        if h == password:
            return count
    return 'Not Found Your Password'


def checkPwnedAPI(password):
    sha1Password = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first5Letter= sha1Password[:5]
    tail = sha1Password[5:]
    response = requestApiData(first5Letter)
    return getPasswordLeaksCount(response.text,tail)

password = str(input("Please enter Password for Check Data Breach.\n"))
data = checkPwnedAPI(password)
print(data)