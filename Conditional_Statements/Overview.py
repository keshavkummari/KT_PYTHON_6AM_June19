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

# 3. elif

fee_1 = 10

if fee_1 == 20:
   print("1 - Got a true expression value")
   print(fee_1)
elif fee_1 == 15:
   print("2 - Got a true expression value")
   print(fee_1)
elif fee_1 == 10:
   print("3 - Got a true expression value")
   print(fee_1)
else:
   print("4 - Got a false expression value")
   print(fee_1)

print("Good bye!")

#!/usr/bin/python

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess <= number:
    # Another block
    print('No, it is a little less than the number')
    # You can do whatever you want in a block ...
elif guess >= number:
    # Another block
    print('No, it is a little more than the number')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed, after the if statement is executed.


Syntax:

The syntax of the nested if...elif...else construct:

if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
elif expression4:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)
else:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else:
      statement(s)

"""
#!/usr/bin/python

char=input("Please enter any charcter : ")

if ord(char)>=65 and ord(char)<=90:
    print ("You entered an upper case alphabet")
    if char in ['A','E','I','O','U']:
        print ("You entered A vowel.",char)
    else:
        print ("You entered a consonant.", char)
elif ord(char)>=97 and ord(char)<=122:
    print ("You entered a lower case alphabet.", char)
    if char in ['a','e','i','o','u']:
        print("You entered a vowel.", char)
    else:
        print ("You entered a consonant.", char)
else:
    print ("You did not enter an alphabet.", char)

print("We are out of the if..elif block")







