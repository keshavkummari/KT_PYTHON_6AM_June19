"""
class Computer:

    def config(self):
        print("i7, 16gb 5TB")

# Creating an Object
Object_computer1 = Computer()
Object_computer2 = Computer()

# Accessing class behaviours
Object_computer1.config()
Object_computer2.config()
"""
class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu,self.ram)


# Creating an Object
Object_computer1 = Computer("i5","4gb")
Object_computer2 = Computer("i7","6gb")

# Accessing class behaviours
Object_computer1.config()
Object_computer2.config()
