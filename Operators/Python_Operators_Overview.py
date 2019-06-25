"""
# There are 7 types of Operators :

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators


1. Arithmetic Operators

1. +   =	Addition
2. -   =	Subtraction
3. *   =	Multiplication
4. /   =	Division  
5. %   =	Modulus
6. **  =	Exponent
7. //  =	Floor Division

x = 15
y = 4

print(x,id(x),type(x))

print(y,id(y),type(y))

print(f"Addition Operator {x} + {y} : ",x+y)
print(f"Subtraction Operator {x} - {y} : ", x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x ** y =',x**y)

2. Comparison (Relational) Operators

a = 10
b = 20
        # 10 == 20
1. ==	= (a == b) is not true.
2. !=	= (a != b) is true.
3. >	= (a > b) is not true.
4. <	= (a < b) is true.
5. >=	= (a >= b) is not true.
6. <=	= (a <= b) is true.

x = 10
y = 12

print(x,id(x),type(x))

print(y,id(y),type(y))

print('x == y is',x==y)
print('x != y is',x!=y)
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)

3. Assignment Operators

1.   =			x = 5		x = 5
2.  +=			x += 5		x = x + 5	[+= Add AND]
3.  -=			x -= 5		x = x - 5	[-= Subtract AND]
4.  *=			x *= 5		x = x * 5	[*= Multiply AND]
5.  /=			x /= 5		x = x / 5	[/= Divide AND]
6.  %=			x %= 5		x = x % 5	[%= Modulus AND]
7.  //=			x //= 5		x = x // 5	[//= Floor Division]
8.  **=			x **= 5		x = x ** 5	[**= Exponent AND]

a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ",a,b,c,id(a),id(b),id(c),type(c),c)

c += a
print(f"Line 2 - Value of C is : {c}")

c *= a
print(f"Line 3 - Value of C is : {c}")

c /= a
print(f"Line 4 - Value of C is : {c}")

c = 2
c %= a
print(f"Line 5 - Value of C is : {c}")

c **= a
print(f"Line 6 - Value of C is : {c}")

c //= a
print(f"Line 7 - Value of C is : {c}")

4. Logical Operators

1. Logical AND = and
2. Logical OR  = or
3. Logical NOT = not

x = True
y = False

print('x and y is',id(x),id(y),type(x),type(y),x and y)

print(f"x {x} and y {y} Memory Location of x = {id(x)} Memory Location of y = {id(y)} {x and y}")

print(f"x = {x}  y = {y} Memory Location of x = {id(x)} Memory Location of y = {id(y)} {x or y}")

print(f"x : {x}  y : {y} Memory Location of x = {id(x)} Memory Location of y = {id(y)} {not x}")

5. Bitwise Operators

Bitwise operator works on bits and performs bit-by-bit operation.

Operator	Meaning	Example
1. &			Bitwise AND	x & y = 0 (0000 0000)
2. |			Bitwise OR	x | y = 14 (0000 1110)
3. ~			Bitwise NOT	~x = -11 (1111 0101)
4. ^			Bitwise XOR	x ^ y = 14 (0000 1110)
5. >>			Bitwise right shift	x>> 2 = 2 (0000 0010)
6. <<			Bitwise left shift	x<< 2 = 40 (0010 1000)

bin()
Prefix : 
0b  : (zero + uppercase letter 'X')
0B  : (zero + uppercase letter 'X')
Interpretation : Binary
Base : 2

oct()
0o  : (zero + uppercase letter 'X')
0O  : (zero + uppercase letter 'X')
Interpretation : Octal
Base : 8

hex()
0x  :  (zero + lowercase letter 'x')
0X  :  (zero + uppercase letter 'X')
Interpretation : Hexadecimal
Base : 16

#True  = 1
#False = 0

a=15
b=10

print(f"a value is {a} Binary Value a {bin(a)}")
print(f"b value is {b} Binary Value of b {bin(b)}")

print(f"Binary of AND & {bin(a&b)}")

0b1111
0b1010

0b1010

a=15
b=10

print(bin(a))
'0b1111'

print(bin(b))
'0b1010'

print(bin(a|b))
'0b1111'

0b1111
0b1010

0b1111

a=15
b=10

# Bitwise XOR OPERATION:
print(bin(a))
'0b1111'

print(bin(b))
'0b1010'


print(bin(a^b))
'0b101'

0b1111
0b1010
-------
0b0101

True+True = False
1+1 = False

1 True + 0 False = True 
  
  0101  # Output 1+1=0 1+0=1 1+1=0 1+0=1
  (Bits has to be differenet then its true condition)


# 5. Bitwise Operators

# Bitwise operators in Python :

Operator	Meaning	Example
1. &			Bitwise AND	x & y = 0 (0000 0000)
2. |			Bitwise OR	x | y = 14 (0000 1110)
3. ~			Bitwise NOT	~x = -11 (1111 0101)
4. ^			Bitwise XOR	x ^ y = 14 (0000 1110)
5. >>			Bitwise right shift	x>> 2 = 2 (0000 0010)
6. <<			Bitwise left shift	x<< 2 = 40 (0010 1000)

#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101

print ('a=',a,':',bin(a),'b=',b,':',bin(b))

c = 0

c = ~a
print ("result of COMPLEMENT is ", c,':',bin(c))

#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101

print ('a=',a,':',bin(a),'b=',b,':',bin(b))

c = 0 

c = ~a
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2
print(f"Left Shift {c} : {bin(c)}")

c = a >> 2
print(f"Right Shift {c} : {bin(c)}")

# Membership Operators 

They are used to test whether a value or variable is found in a sequence
(String, List, Tuple, Dictionary & Set)

1. in
2. not in 

x = 'Hello world'
y = {1:'a',2:'b'}

print('W'.lower() in x)

print(1 not in y)

7. Identity Operators

Used to check if two values or variables are located on the same part of the memory.

1. is
2. is not

x1 = 5
y1 = 5

x2 = 'Hello'
y2 = 'Hello'

x3 = [1,2,3]
y3 = [1,2,3]

print(f"Memory Location of Variable x1 {x1} {id(x1)}")
print(f"Memory Location of Variable y1 {y1} {id(y1)}")
print("")
print(f"Condition using Identity Operator : {x1 is y1}")
print("")
print(f"Memory Location of Variable x2 {x2} {id(x2)}")
print(f"Memory Location of Variable y2 {y2} {id(y2)}")
print("")
print(f"Condition using Identity Operator : {x2 is y2}")
print("")
print(f"Memory Location of Variable x3 {x3} {id(x3)}")
print(f"Memory Location of Variable y3 {y3} {id(y3)}")
print("")
print(f"Condition using Identity Operator : {x3 is not y3}")
print("")

"""






