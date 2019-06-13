            #01234567   Left to Right Indexing
            #abcdefgh

            # -8 -7 -6 -5 -4 -3 -2 -1   Right to Left Indexing
            #  a  b  c  d  e  f  g  h

alphabets = 'abcdefgh'

print(alphabets,type(alphabets),id(alphabets),len(alphabets))

# Left to Right Indexing
print(alphabets[0])
print(alphabets[7])

# Right to Left Indexing
print(alphabets[-1])
print(alphabets[-8])

