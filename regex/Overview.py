
#import regex 
# R'expression' or r'expression'

"""
# Basic patterns which match single chars :

a, X, 9, <      -- ordinary characters just match themselves exactly.
. (a period)    -- matches any single character except newline '\n'
\w              -- matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].
\W              -- matches any non-word character.
\b              -- boundary between word and non-word
\s              -- matches a single whitespace character -- space, newline, return, tab
\S              -- matches any non-whitespace character.
\t, \n, \r      -- tab, newline, return
\d              -- decimal digit [0-9]
^                = matches start of the string
$                = match the end of the string
\               -- inhibit the "specialness" of a character.
"""

"""
# Compilation flags :

Compilation flags let you modify some aspects of how regular expressions work.

Flags are available in the re module under two names,

a long name such as IGNORECASE and a short, one-letter form such as I.

---------------------------------------------------------------
Flag	        Meaning
---------------------------------------------------------------
ASCII, A	  Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
DOTALL, S	  Make . match any character, including newlines
IGNORECASE, I	  Do case-insensitive matches
LOCALE, L	  Do a locale-aware match
MULTILINE, M	  Multi-line matching, affecting ^ and $
VERBOSE, X   (for ‘extended’)  Enable verbose REs, which can be organized more cleanly and understandably
"""


