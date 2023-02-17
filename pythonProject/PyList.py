# Lists in python
# Lists are a sequential data type
pList = ['1', 1, 2, "Sample", 3.3, True]
# Iterating through list using indices
for i in range(len(pList)):
    print(pList[i])

# Slicing can be done for list as for strings

print(pList[0:2])

stri = "Happy"

print(stri+" New Year")

# similarly lists can be concatenated

print(pList+["New", "Year"])

# List is mutable however, strings are not (means lists can be assigned and replaced values specific indexes)

pList[0] = "Replaced 1 with 0 at zeroeth index"

print(pList)


# Lists can be nested
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("Nested List: ", x)

# unpacking a collection

s = ["alpha", "omega", "sigma", "delta"]
a, b, c, d = s  # unpacking a collection by assigning a list to the variables

print(a, b, c, d)

for i in s:
    print(i, end="\t")

s.append("gamma")
print("New list s: ", s)

# shorthand for loop

[print(x, end=',') for x in s]

[print(x) for x in s]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

nfruits = [x for x in fruits]

print(nfruits)
print(nfruits)

t = ("apple", "mango", "berry")

t.__add__(t)

print(t)