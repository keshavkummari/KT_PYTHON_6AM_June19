"""
An updated version of test_patterns() that shows the numbered and named
groups matched by a pattern will make the following examples easier to follow.
"""
import re

def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Show the character positions and input text
    print()
    print(''.join(str(i/10 or ' ') for i in range(len(text))))
    print(''.join(str(i%10) for i in range(len(text))))
    print(text)

    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print()
        print('Matching "%s"' % pattern)
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print('  %2d : %2d = "%s"' % \
                (s, e-1, text[s:e]))
            print('    Groups:', match.groups())
            if match.groupdict():
                print('    Named groups:', match.groupdict())
            print()
    return

test_patterns('abbaaabbbbaaaaa',
              [r'a((a*)(b*))', # 'a' followed by 0-n 'a' and 0-n 'b'
               ])
