import xml.sax


class ABContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        print("startElement '" + name + "'")
        if name == "address":
            print("\tattribute type='" + attrs.getValue("type") + "'")

    def endElement(self, name):
        print("endElement '" + name + "'")

    def characters(self, content):
        print("characters '" + content + "'")


def main(sourceFileName):
    source = open(sourceFileName)
    xml.sax.parse(source, ABContentHandler())


if __name__ == "__main__":
    main("addressbook.xml")