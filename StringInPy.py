# Besides numbers, Python can also manipulate strings, which can be expressed in several ways.
# They can be enclosed in single quotes ('...') or double quotes ("...") with the same result 2.
# \ can be used to escape quotes:

print('spam egss')  # single quotes 'spam eggs'
print('doesn\'t')   # use \' to escape the single quote..."doesn't" '\' escapes the special meanings
print("doesn't")   # ...or use double quotes instead "doesn't"
print('"Yes," they said.')      # '"Yes," they said.'
print("\"Yes,\" they said.")    # '"Yes," they said.'
print('"Isn\'t," they said.')   # '"Isn\'t," they said.'
print('First line.\\n Second line')  # \n meaning is skipped due to '\' character
print('First line.\n Second line')
print('C:\some\name')
print("Some\\name")
# If you don’t want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote:'''
print(r'C:\some\name')

# String literals can span multiple lines.
# One way is using triple-quotes: """...""" or ''''...''''.
# End of lines are automatically included in the string,
# but it’s possible to prevent this by adding a \ at the end of the line. The following example:
# produces the following output (note that the initial newline is not included):
'''Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to'''
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
# 3 times 'un', followed by 'ium'
print('un' * 3 + 'ium')  # 'unununium'same result is produced by 3 * 'un' + ium

'''Two or more string literals (i.e. the ones enclosed between quotes) 
next to each other are automatically concatenated.'''

print('Py' 'thon')
'''This feature is particularly useful when you want to break long strings:'''

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

'''This only works with two literals though, not with variables or expressions:'''
prefix = 'Py'
suffix = 'thon'
# print(prefix+suffix) # This works ! Prints Python
# print(prefix suffix) # This doesn't work. Incorrect syntax-can't keep two variables together and concatenate
# print(prefix'thon')  # Neither this works
# print(('un' * 3) 'ium') #Nor this works
print("STR1"+"STR2")
'''to concatenate strings use the '+' operator'''
print(prefix+'thon')

# Strings can be indexed (subscripted), with the first character having index 0.
# There is no separate character type; a character is simply a string of size one:'''

word = 'Python'
print(word[0])  # character in position 0 -> 'P'
print(word[5])  # character in position 5 -> 'n'

'''Indices may also be negative numbers, to start counting from the right:'''
print(word[-1])  # last character ->'n'
print(word[-2])  # second-last character -> 'o'
print(word[-6])  # First character -> 'P'
print(word[0])   # Prints 'P'
# Note that since -0 is the same as 0, negative indices start from -1.
# In addition to indexing, slicing is also supported.
# While indexing is used to obtain individual characters, slicing allows you to obtain substring:'''

print(word[0:2])  # Prints 0th (0 included) (2 excluded) till 1st character i.e. 'Py' and does not include the 2nd character

print(word[2:4])  #  Print 'th' from Python second included 4th character excluded

# Slice indices have useful defaults; an omitted first index defaults to zero,
# an omitted second index defaults to the size of the string being sliced

print(word[:2])   # character from the beginning to position 2 (excluded) 'Py'
print(word[4:])   # characters from position 4 (included) to the end 'on'
print(word[-2:])  # characters from the second-last (included) to the end 'on'

# Note how the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s:

print(word[:2]+word[2:])  # Prints 'Python' thus s[:i]+s[i:] = s

# But this does not print Python , instead prints 'thonPy'
print(word[2:]+word[:2])

# Similarly,Prints 'Python' thus s[:i]+s[i:] = s
print(word[:4]+word[4:])

# One way to remember how slices work is to think of the indices as pointing between characters,
# with the left edge of the first character numbered 0.
# Then the right edge of the last character of a string of n characters has index n, for example:

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# For non-negative indices, the length of a slice is the difference of the indices,
# if both are within bounds. For example, the length of word[1:3] is 2.

# Attempting to use an index that is too large will result in an error:
# print(word[42])  # Throws index out of range error

# However, out of range slice indexes are handled gracefully when used for slicing
print(word[2:45])  # even though out of range slicing recalibrates out of range to string length prints string slice

# Python strings cannot be changed — they are immutable.
# Therefore, assigning to an indexed position in the string results in an error:

# word[0] ='J'  # TypeError: 'str' object does not support item assignment

# word[2:] = 'py'  # TypeError: 'str' object does not support item assignment

# If you need a different string, you should create a new one:

new_word = 'J' + word[1:]

print(new_word)

print(word[:2] + 'py')

# The built-in function len() returns the length of a string:

print(len(new_word))  # Prints 6

s = 'supercalifragilisticexpialidocious'

print(len(s))

# What are literals?
# Ans - Literals are notations for constant values of some built-in types
# Text Sequence Type — str
#  String literals
# Textual data in Python is handled with str objects, or strings.
# Strings are immutable sequences of Unicode code points.
# String literals are written in a variety of ways:
# Single quotes: 'allows embedded "double" quotes'
# Double quotes: "allows embedded 'single' quotes"
# Triple quoted: '''Three single quotes''', """Three double quotes""". These can span multiple lines

# Byte literals are named with prefixes b or B
# Both byte and str literals can be written in single, double or triple-single and triple-double quote
# The backslash (\) character is used to escape characters that otherwise have a special meaning,
# such as newline, backslash itself, or the quote character.

# RAW STRINGS
# Both string and bytes literals may optionally be prefixed with a letter 'r' or 'R';
# such strings are called raw strings and treat backslashes as literal characters.
# As a result, in string literals, '\U' and '\u' escapes in raw strings are not treated specially.

# STR CONSTRUCTOR
# Strings may also be created from other objects using the str constructor.
# Since there is no separate “character” type, indexing a string produces strings of length 1.
# That is, for a non-empty string s, s[0] == s[0:1]
# class str(object='')
# class str(object=b'', encoding='utf-8', errors='strict')-- Returns an object of type string

my_name = str('Mervin')
my_bname = str(b'Mervin')

print("My name is created using built-in str() constructor: ", my_name)
print ("Type of the object my_name is : ", type(my_name))


print("My 'b'name is created using built-in str() constructor: ", my_bname)
print ("Type of the object my_name is : ", type(my_bname))
num = str(3)  # Returns 3 as a string
print("type of num created by str() constructor with val 3 : ", num, "Type of num :", type(num))

# class object() is a base for all classes
# __str__() is called by str(object) constructor- this print informal or nicely printable string representation
# if any object does not have the __str__() then it defaults to repr(object) __repr__()
# repr(object internally calls __repr__() method
# __repr__() method is used to print the formal/official string representation of the object
# if any object doesn't have __str__() then it uses __repr__() to print informal string representation

print()

# STRING METHODS
# link - https://docs.python.org/3/library/stdtypes.html#string-methods
# 1. str.capitalize() -
# Return a copy of the string with its first character capitalized and the rest lowercased
print(str.capitalize("mervin"))

# count() method for counting the number of instances od substring within a main string
str_cnt = 'Thisisacounttest'
print(" str.cnt function demo : ",str_cnt.count("is", 0, 4))  # the 0 and 4 are optional

# expandtabs() method to replace tab with spaces
str_tab = '01\t012\t0123\t01234'
print(str_tab.expandtabs(3))

# 01 012   0123  01234
print(str_cnt[0:7])

# find() function for str objects
print("Find method ", str_cnt.find("count", 7, len(str_cnt)))

# Use find method only to find the lowest index of the substring in a string
# to check if a substring is present in a string or not use 'in' operator
print("Is count present in str_cnt?", "count" in str_cnt)

# format() method for performing string fomatting
sum = 1+2
this = "this"
print("The sum of 1 + 2 is {0}".format(sum))

print("The sum of 1 + 2 is {} {}".format(sum, this))

# index() method is also returns the lowest index like find()

# isalpha() method returns true if there is atleast one character and all the characters are alphabets

str_isalpha = 'c'
print("Is str_isalpha? : ", str_isalpha.isalpha())
print("Is str_isalpha decimal ? : ", str_isalpha.isdecimal())

# isdecimal()
str_decimal = '123'
print("Is str_decimal? decimal ?: ", str_decimal.isdecimal())

str_decimal_2 = '123.123'
print("Is str_decimal_2 decimal ? :", str_decimal_2.isdecimal())

# isdigit()
str_isdigit = '12ab'
print("Is str_isdigit digit? : ", str_isdigit.isdigit())
print("Is str_isdigit numeric? : ", str_isdigit.isnumeric())

str_isdigit_1 = '.'
print("Is str_isdigit_1 numeric? : ", str_isdigit_1.isnumeric())
print("Is str_isdigit_1 numeric? : ", str_isdigit_1.isdecimal())
print("Is str_isdigit_1 numeric? : ", str_isdigit_1.isdigit())

# isnumeric()
str_numeric = '123'
print("Is str_numeric numeric? : ", str_decimal.isnumeric())

str_numeric_1 = '123.123'
print("Is str_numeric_1 numeric? : ", str_numeric_1.isnumeric())

''''
str.isascii()
str.isidentifier()
keyword.iskeyword()
str.islower()
str.isprintable()
str.isspace()
str.istitle()
str.isupper()
str.join(iterable)
str.ljust(width[, fillchar])
str.lower()
str.lstrip([chars])
static str.maketrans(x[, y[, z]])
str.partition(sep)
str.removeprefix(prefix, /)
str.removesuffix(suffix, /)
str.replace(old, new[, count])
str.rfind(sub[, start[, end]])
str.rindex(sub[, start[, end]])
str.rjust(width[, fillchar])
str.rpartition(sep)
str.rsplit(sep=None, maxsplit=- 1)
str.rstrip([chars])
str.split(sep=None, maxsplit=- 1)
str.splitlines(keepends=False)
str.startswith(prefix[, start[, end]])
str.strip([chars])
str.swapcase()
str.title()
string.capwords()
str.translate(table)
str.upper()
str.zfill(width)'''

# Formatted string literals are strings prefixed with f or F
# These strings may contain replacement fields, which are expressions delimited by curly braces {}
# formatted strings are really expressions evaluated at run time




