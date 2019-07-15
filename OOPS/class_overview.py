# Creating a Class
class Human():
    def __init__(self,name,gender):  # Constructer or Inializer
        self.name = name             # Instance Variables
        self.gender = gender         # Instance Variables
    
    def speak_name(self):
        print("My Name is %s" % self.name)

    def speak(self,text):
        print(text)

# Creating an Object

kt = Human('Mary','F')

#print(kt)
#print(type(kt))

#print(kt.name)
#print(kt.gender)
kt.speak_name()
kt.speak('Welcome to Python World')


