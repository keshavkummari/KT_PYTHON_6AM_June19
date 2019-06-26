#!/usr/bin/python

# name = "Guido van rossum"

"""
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
print('keshav Kummari'.istitle())

"""
18	join(seq)
	Merges (concatenates) the string representations of elements in sequence seq into a string,
	with separator string.
"""	

s = "  &  "
seq = ("a", "b", "c") # This is sequence of strings.

print(s.join(seq))

# a  &  b  &  c  &

joiner = "-"

title="10 20 30 Abc"

print(joiner.join(title))

"""
