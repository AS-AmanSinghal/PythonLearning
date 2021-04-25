import re

string = 'Search of this text this adha'

a = re.search('this',string)
print(a.span())
print(a.start())
print(a.group())
print(a.end())



pattern = re.compile('Search of this text this')

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.group())
print(b)
print(c)
print(d)
