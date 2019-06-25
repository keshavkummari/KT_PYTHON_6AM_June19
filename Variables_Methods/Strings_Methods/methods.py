#!/usr/bin/python

name = "Guido van rossum"

print(f"Accessing a Variable : {name}")

print(f"Capitalize : {name.capitalize()}")

print(f"UpperCase : {name.upper()}")

name1 = "GUIDO VAN ROSSUM"

print(f"LowerCase : {name1.lower()}")

print(name.isupper())
print(name1.isupper())

print(name.islower())
print(name1.islower())

print(name.istitle())
print(name1.istitle())

print(name.swapcase())
print(name1.swapcase())
