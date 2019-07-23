# Match Function 

import re

line = "Welcome to PYTHON World By Keshav Kummari"

matchObj = re.match(r'(.*)python(.*)',line,re.M|re.I)

if matchObj:
    print(matchObj.group())
    print(matchObj.groups())
else:
    print("No Match Found!")