class Animal:
    def __init__(self,name):
        self.name = name 
    
    def talk1(self):
        print(self.name, "Welcome to Animal World")

class Cat(Animal):
    def talk2(self):
        print(self.name, "Welcome to Cat World")

class Dog(Cat,Animal):
    def talk3(self):
        print(self.name, "Welcoem to Dog World")

a = Dog('Nick')
a.talk1()

a = Dog('Tomy')
a.talk2()

a = Dog('Jer')
a.talk3()



"""
class Animal():
    def __init__(self):
        print("Animal Created!")
    
    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating...")
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def whoAmI(self):
        print("Dog")
    
    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()
"""