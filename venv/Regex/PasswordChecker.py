import re

pattern = re.compile(r"^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$")

string = "nn@nnnNN892310"

a = pattern.search(string)
b = pattern.fullmatch(string)
print(a)
print(b)

