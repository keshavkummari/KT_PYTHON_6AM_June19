"""

1. The 1. if  2. if..else , 3. elif  and 4. neasted elif

Syntax :

# 1. Simple if condition

if expression:
    statement(s)

name = input("Enter your UserName : ")

if name == "kt1020":
    print(f"Welcome,{name}")

print("I am out side of if block")

# if..else

name = input("Enter your UserName : ")

if name == "kt1020":
    message = f"Welcome to {name}"
else:
    message = f"Invalid UserName {name}"

print(message)

"""

# 3. elif


fee_1 = 10

if fee_1 == 20:
   print("1 - Got a true expression value")
   print(fee_1)
elif fee_1 == 15:
   print("2 - Got a true expression value")
   print(fee_1)
elif fee_1 == 12:
   print("3 - Got a true expression value")
   print(fee_1)
else:
   print("4 - Got a false expression value")
   print(fee_1)

print("Good bye!")
