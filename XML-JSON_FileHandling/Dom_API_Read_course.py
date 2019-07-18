from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("/Users/keshav/KT_PYTHON_6AM_June19/XML-JSON_FileHandling/movies.xml")

collection = DOMTree.documentElement

if collection.hasAttribute("shelf"):
    print("Root Element : %s " %(collection.getAttribute("shelf")))

m = collection.getElementsByTagName("movie")

for i in m:
    print("----------------Movies----------")

    if i.hasAttribute("title"):
        print("Title : %s " %(i.getAttribute("title")))

    type = i.getElementsByTagName('type')[0]
    print("Type: %s" % type.childNodes[0].data)

    format = i.getElementsByTagName('format')[0]
    print("Format: %s" % format.childNodes[0].data)

    rating = i.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)

    description = i.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)
