"""
# Loops in Python

1. While

2. For

# Loop Controls

1. Continue

2. Break


1. while 

while condition:
    statement(s)
   
raw_data = int(input("Enter a Number : "))

while raw_data <= 10:
    print(f"I am a While Loop : {raw_data}")
    raw_data = raw_data + 1    

passWord = ""

print(passWord,type(passWord),id(passWord),len(passWord))

while passWord != "redhat":
    passWord = input("Please enter the password: ")

    if passWord == "redhat":
        print("Correct password")

    elif passWord == "admin@123":
        print("It was previously used password")

    elif passWord == "Redhat@123":
        print("This is your recent changed password")

    else:
        print("Incorrect Password- try again")


counter = 0

while counter < 3:
    print(f"Inside WHILE Loop {counter}")
    counter = counter + 1
else:
    print(f"I am a Else Block {counter}")
    

invalid = True

while invalid:
    number = int(input("Please enter a number in the range 10 to 20: "))
    if number >= 10 and number <= 20:
        invalid = False
    else:
        print("Sorry number must be between 10 and 20")
        print("Please try again")

print("You entered {0}".format(number))
print("This is a valid number")


#name = input("Enter Your Name : ")  # Guido Van Rossum

for i in name:
    print(i)  
      
for a in range(0,10): # stop-1 end-1 10-1 9 (0,1,2,3,4,5,6,7,8,9)
    if (a in range(5,8)):
        print(f"{a} is Matching")
        continue
    else:
        print(a)      
"""



count=0


name=input("Enter Your Name to Find out No.of Vowels : ")

for letter in name:
    if (letter in ['A','E','I','O','U','a','e','i','o','u']):
        count=count+1

print (f"You have {count} Vowels in your name")


