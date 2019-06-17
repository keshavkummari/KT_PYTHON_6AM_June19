            #01234567   Left to Right Indexing
            #abcdefgh

            # -8 -7 -6 -5 -4 -3 -2 -1   Right to Left Indexing
            #  a  b  c  d  e  f  g  h
            #012345
"""
alphabets = 'abcdefgh'

print(alphabets,type(alphabets),id(alphabets),len(alphabets))

# Left to Right Indexing
print(alphabets[0])
print(alphabets[7])

# Right to Left Indexing
print(alphabets[-1])
print(alphabets[-8])
                #  0 is Start Index and 6 is ending index 6-1 5 012345
print("Range Slice",alphabets[0:6]) # [:] Range Slice [0:6]
print(alphabets[:])
print(alphabets[:6])
print(alphabets[:-1])
"""
          #01234567891011121314
numbers = "102030405060708090"

print(numbers[0::3]) # Zero Based Indexing

print(numbers * 5)

firstname,middlename,lastname = "Guido",'Van',"Rossum"

print(firstname + middlename + lastname)

print(f"{firstname} {middlename} {lastname}")
