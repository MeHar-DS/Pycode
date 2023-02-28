# A set is an unordered collection with no duplicate elements
# Basic uses include membership testing and eliminating duplicate entries
# Set object also supports mathematical operations like Union, intersection, difference, symmetrical difference
# Curly braces or the set() function can be used ot create a set
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

print(basket)  # To demonstrate that duplicates are removed

print("orange" in basket)

print("crabgrass" in basket)

# Demonstrate set operations on unique letters from two words

a = set("abracadabra")
b = set("alacazam")

print(a)  # This prints unique letters in set a
print(b)  # This prints unique letters in set b

print(a-b)  # print unique letters in a but not in b

print(a | b)  # print unique letters in a or b or both

print(a & b)  # print unique letters in both a and b

print(a ^ b)  # print unique letters in a or b but not in both


# Similarly to list comprehensions there is set comprehensions

setcomp = {x for x in "abracadabra" if x not in "abc"}

print(setcomp)
