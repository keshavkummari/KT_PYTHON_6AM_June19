#/usr/bin/python
# A-Z     # Hash means single line comment
# a-z
# combinations of A-Z & a-z
# 0-9
# combinations of A-Z , a-z & 0-9
# an underscore (_).
# combinations of A-Z , a-z , 0-9 & _



"""
a = 1
A = 2
highScoreValue = 1
HighScore = 2
aVariable_check=10
_id = 1020

print(a,A,highScoreValue,HighScore,aVariable_check,_id)

Data Types :

Numbers
Strings
List
Tuple
Dict
Set

int()
str()
list()
tuple()
dict()
set()
"""

# Single Line Comment

'#! = Shebang'

"/usr/bin/python = Absolute path of the python"

# Multi-line comments

"""
Today we are discussing about
Python.

Python 2.x
And
Python 3.x 
"""

'''
Today we are discussing about
Python.

Python 2.x
And
Python 3.x 
'''

#Python Code >> Compiler >> Python Byte Code >> Python Virtual Machine >> Machine Code

"""
# Numbers

a = 10

b = 10.75

c = 3 + 4j

print(a,type(a))
print(b,type(b))
print(c,type(c))

# Strings

first_name = 'Guido'
middle_name = "Van"
last_name = '''Rossum'''
language = 'Python'

print(first_name,type(first_name),id(first_name),len(first_name))
print(middle_name,type(middle_name),id(middle_name),len(middle_name))
print(last_name,type(last_name),id(last_name),len(last_name))
print(language,type(language),id(language),len(language))

raw_data, processed_data, final_data = 'It has 1000 records', 700 , "500 Records"

print(raw_data)
print(processed_data)
print(final_data)

raw_data=processed_data=final_data='100 Records'

print(raw_data)
print(processed_data)
print(final_data)

"""

# List (Mutable Data Type)

'''
list()

courses = ['Python','AWS','AZURE','DevOps',10,23.75,3+5j,'@gmail.com']

print(courses,type(courses),id(courses),len(courses))

print(list(enumerate(courses)))

courses.append('Terraform')
courses.remove('AZURE')

print(courses,type(courses),id(courses),len(courses))
print(list(enumerate(courses)))
'''

# Tuple Data Type (Immutable Data TYpe)

'''
tuple()

technologies_list = ('Python','AWS','AZURE','DevOps',10,23.75,3+5j,'@gmail.com')
_list = 'Python','AWS','AZURE','DevOps',10,23.75,3+5j,'@gmail.com'

print(technologies_list,type(technologies_list),id(technologies_list),len(technologies_list),tuple(enumerate(technologies_list)))

print(_list,type(_list),id(_list),len(_list),tuple(enumerate(_list)))
'''

# Dictionaries  (Mutable Data Type)

dict()

course = {'Name':'Guido','Account_number':101005067,'Branch':'Hyderabad'}

print(course,type(course),id(course),len(course),dict(enumerate(course)))

print(course['Name'])

course['Bank Name']='SBI'

print(course)

# Set

set()

#a = set(('Python','AWS','AZURE','DevOps','Python','AWS','AZURE','DevOps'))
# a = set(['Python','AWS','AZURE','DevOps','Python','AWS','AZURE','DevOps'])

a = set({'Name':'Guido','Account_number':101005067})

print(a,type(a),id(a),len(a),set(enumerate(a)))
