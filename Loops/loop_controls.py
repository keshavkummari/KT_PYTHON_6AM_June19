#!/usr/bin/python

for i in range(0,16): # end-1 16-1 = 15
	if (i in range(9,14)): # end-1 14-1 = 13
		print(f"{i} is matching")
		break
	else:
		print(f"{i}")

print("I am outside of the loop block")
