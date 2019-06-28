
languages = {'firstname':'Guido','middlename':'Van','lastname':'Rossum'}


print(languages.get('firstname'))

print(languages.get('Guido'))

print(languages.keys())

print(languages.values())

print(languages.items())

seq_tuple = ('name','age','gender')

print(languages.fromkeys(seq_tuple,0))

print(languages)