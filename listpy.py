# List - https://docs.python.org/3/tutorial/introduction.html

''''Python knows a number of compound data types, used to group together other values.
The most versatile is the list, which can be written as a list of comma-separated values (items)
between square brackets. Lists might contain items of different types, but usually the items all have the same type.'''

squares = [1, 4, 9, 16, 25]

print(squares)

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
print(squares[0]) # indexing returns the item -> 1
print(squares[-1]) # 25
print(squares[-3:]) # slicing returns a new list --> [9, 16, 25]

# All slice operations return a new list containing the requested elements.
# This means that the following slice returns a shallow copy of the list:

print(squares[:])

# Lists also support operations like concatenation:

print(squares + [36, 49, 64, 81, 100])

'''' Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:'''
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4 ** 3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes) # [1, 8, 27, 64, 125]

# You can also add new items at the end of the list, by using the append() method
# (we will see more about methods later):
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)  # [1, 8, 27, 64, 125, 216, 343]

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] =['C','D','E']  # replace some values
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] =[]

print(letters)

# The built-in function len() also applies to lists:

letters = ['a','b','c','d','d']
print(len(letters))

# It is possible to nest lists (create lists containing other lists), for example:

a = ['a','b','c','d']
b = [1,2,3]
c = [a,b]  # Nesting of lists is creating list within list

print(c)
print(c[1][1])
print(c[-1][-1])
# need to explore the list functions further
