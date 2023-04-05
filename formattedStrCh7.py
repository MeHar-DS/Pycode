# Formatted string literals using f or F symbol

year = 2016
event = 'Referendum'

print(f'Event for the grand {event} to be conducted in {year}')

# Formatted string literals lets us have an expression inside a string

import math
print(f'The value of pi is approximately{math.pi:.3f}.')

# Passing an integer after the  ':' will cause that field to be a minimum number of charachters wide.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name,phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# Other modifiers such as !a applies ascii !s applies str() and !r applies repr()

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {repr(animals)}')
print(f'My hovercraft is full of {animals!r}')  # Same as above line


# The = specifier can be used to expand an expression to the text of the expression, an equal to sign
# and then representation of the evaluated expression

bugs = "roaches"
count = 13
area = 'living room'

print(f'Debugging {bugs=} {count=} {area=}')

# str.format method

yes_votes = 42_572_654
no_votes = 43_132_495

percentage = yes_votes/(yes_votes+no_votes)

print('{:-9} YES Votes {:2.2%}'. format(yes_votes, percentage))

# Another example for format method

print('We are the ones {} who say "{}!"'.format('knights', 'Ni'))

# A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

print('{0} {1}'.format('spam', 'eggs'))
print('{1} {0}'.format('spam', 'eggs'))

# IF keyword arguments are used in the str.format() method, their values are referred
# to by using the name of the argument

print('This {food} is {adjective}'. format(food='spam', adjective='absolutely horrible'))

# Positional and keyword argument can be arbitrarily used

print('The story of {0} {1} and {other}.'.format('Bill', 'Manfred', other='Georg'))

# if you have a really long format string that you dont want to split up, it would be nice if
# you could reference the variables to be formatted by name instead of by position
# this can be done by simply passing the dict and using the square bracket '[]' to access the keys as shown below:

table ={'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

#This could also be done by passing the table dictionary as keyword arguments with the ** notation

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
