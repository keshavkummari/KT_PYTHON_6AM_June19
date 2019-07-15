
class exClass:
    eyes = "Brown"
    age  = "30"

    def echoName(self):
        print(self.eyes)
        print(self.age)
        return "Hello"


exObject = exClass()
exObject.eyes
exObject.age

exObject.echoName()