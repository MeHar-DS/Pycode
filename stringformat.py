# https://docs.python.org/3/library/string.html#formatstrings
# str.format() is the function used
# formatted string literal - https://docs.python.org/3/reference/lexical_analysis.html#f-strings

''''Format strings contain “replacement fields” surrounded by curly braces {}.
Anything that is not contained in braces is considered literal text,
which is copied unchanged to the output. If you need to include a brace character in the literal text,
it can be escaped by doubling: {{ and }}.'''

strform = "This is a text for {{format}}"

print("checks for {0}".format(strform))

# print("checks for {1}".format(strform))  # IndexError: Replacement index 1 out of range for positional args tuple

first= "1"
second ="2"

print("First {} second {}".format(first,second))
#Same as above
print("First {0} second {1}".format(first,second))

# format examples - https://docs.python.org/3/library/string.html#formatexamples
# more complex examples can be referred at the link above

print("{0} {1} {2}".format("This", "is", "format behavior"))

print('{}, {}, {}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

# Unpacking behavior
print('unpacking behavior :{2}, {1}, {0}'.format(*'abc'))

print('{0}{1}{0}'.format('abra', 'cad'))   # arguments' indices can be repeated

# Accessing arguments by name:

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))  # 'Coordinates: 37.24N, -115.81W'

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))  # 'Coordinates: 37.24N, -115.81W'

