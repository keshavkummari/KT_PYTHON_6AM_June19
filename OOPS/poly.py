class India():

    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")

    def type(self):
        print("Developing")

class USA():

    def capital(self):
        print("Washington DC")

    def language(self):
        print("English")

    def type(self):
        print("Developed")


obj_india = India()
#obj_india.capital()
#obj_india.language()
#obj_india.type()

obj_usa = USA()
#obj_usa.capital()
#obj_usa.language()
#obj_usa.type()

for i in (obj_india,obj_usa):
    i.capital()
    i.language()
    i.type()

"""
class Document:
    def __init__(self,name):
        self.name = name 
    
    def show(self):
        raise NotImplementedError("SubClass Must Implement Abstract Method")
    
class Pdf(Document):
    def show(self):
        return "Show PDF Contents!"
    
class Word(Document):
    def show(self):
        return "Show Word Contents!"

documents = [Pdf('Document1'),Word('Document2')]

for i in documents:
    print(i.name + ':' + i.show())
    
"""