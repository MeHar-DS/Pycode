# List comprehensions provide a concise way to create lists. Common applications are to
# make new lists where each element is the result of some operations applied to each member
# of another sequence or iterable, or to create a subsequence of those elements that satisfy
# a certain condition

# Consider the below function to create squares:

squares= []

for x in range(10):
    squares.append(x**2)

print(squares)

# Alternative-2
squares = list(map(lambda x: x**2, range(10)))

print(squares)

# List comprehension alternative - shortest

squares = [x**2 for x in range(10)]

print(squares)

# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating
# the expression in the context of the for and if clauses which follow it.
# For example, this listcomp combines the elements of two lists if they are not equal:

# listcomprehension with two variables and multiple for loops and if conditions

listcomp = [(x,y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print("Listcomp:", listcomp)

# Example 2

vec = [-4, -2, 0, 2, 4]

# Create a new list with the values doubled
newLstValDouble = [x*2 for x in vec]
print("New list with values doubled : ", newLstValDouble)

# Filtering negative values
lstFilterNeg = [x*2 for x in vec if x >= 0]
print("Filtered neg values: ", lstFilterNeg)

# Applying a function to all elements
print([abs(x) for x in vec])

# Call a method on each element
freshfruit = ['    banana  ', "     loganberry  ", '    passionfruit  ']
print("List entries before function application :", freshfruit)
funAppliationOnList = [f.strip() for f in freshfruit]
print("List entries after function application :", funAppliationOnList)

# Create a list of 2-tuples like (number, square)
# print("Tuple with number and its square.")
print("Tuple with number and its square.", [(x, x**2) for x in range(6)])

# The tuple must be parenthesised otherwise error is raised
# [x,x**2 for x in range(6)]

# Flatten a list using a listcomp with two "for"
vec =[[1,2,3], [4,5,6], [7,8,9]]
print("vec before filtering: ", vec)
vec =[x for val in vec for x in val]
print("vec after filtering:", vec)

# List comprehensions can contain complex expressions and nested functions

from math import pi
print("Rounding the value of pi with different decimal magnitude values of i: ",
      [str(round(pi, i)) for i in range(1, 6)])


# Nested list comprehensions
targ = []
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

for i in range(len(matrix)+1):
    targ.append([row[i] for row in matrix])

print(targ)

# Smarter Nested list comprehension alternative
nestlstcomp = []

nestlstcomp = [[row[m] for row in matrix] for m in range(4)]

print(nestlstcomp)

# Implementing the above feature using zip function
ziplist = list(zip(*matrix))

print(ziplist)