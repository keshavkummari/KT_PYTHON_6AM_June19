class P:
    def __init__(self,name,alias):
        self.name = name            # Public Class Property
        self.__alias = alias        # Private Class Property

    def who(self):
        print("Name  : ", self.name)
        print("Alias : ", self.__alias)

    def __foo(self):                # Private Class Method/Behaviour
        print("This is a Private Method")

    def foo(self):
        print("This is a Public Method")
        self.__foo()

a = P("Guido","GVR")

#a.who()

print(a.name)
print(a._P__alias)
#a.__foo()

#a._P__foo()

#a.foo()
