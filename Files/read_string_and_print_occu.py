# Reading a string and print the occurances 

name = "Guido Van Rossum"

emptyDict = {}

for var in name:                    # G
    if var in emptyDict:            # G in emptyDict 
        print("I am a if Block")
        emptyDict[var] += 1

    else:
        print("I am a Else Block")
        emptyDict[var] = 1          # G emptyDict = {1:G, 2:u, 3:i}
    
print(emptyDict)

https://github.com/keshavkummari/KT_PYTHON_6AM_June19

