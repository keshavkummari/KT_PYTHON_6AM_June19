# Search Function 

import re

line = "Welcome to PYTHON World By Keshav Kummari"

searchObj = re.search(r'(.*)python(.*)',line,re.M|re.I)

if searchObj:
    print(searchObj.group())
    print(searchObj.groups())
else:
    print("No Match Found!")