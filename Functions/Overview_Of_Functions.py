# Functions in Python

# 1. def
# 2. Function Name
# 3. Open & Close Paranthesis  and Parameters
# 4. Colon : Suit
# 5. Indented
# 6. return statement - Exits a Function


"""
def function_name(parameters):
    function_suite
    return [expression]

def sum(var1,var2):
    total = var1 + var2
    print(total)
    return

a = sum(10,20)

#print(a)

"""
# Function Arguments:
'''
You can call a function by using the following types of formal arguments:

1. Required arguments

2. Keyword arguments

3. Default arguments

4. Variable-length arguments

# 1. Required arguments

def sum(var1):
    print(var1)
    return

# Create a Variable
abc = 10

a = sum(abc)

sum(abc)

# 2. Keyword arguments

def hello1(name,age):
    print(name)
    print(age)
    return

hello1(name="Guido Van Rossum",age=50)

# 3. Default arguments

#!/usr/bin/python

# Function definition is here
def info( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call info function
info(name="Guido",age=input("Enter the Age: "))
'''
# 4. Variable-length arguments

def info(*var1):

    for i in var1:
        print(i)
    return

info(10,20,30,40,50,60,70,80,90)

# An Asterisk * is placed before the variable/argument name,
# * holds the values of all the non-keyword variable arguments.
