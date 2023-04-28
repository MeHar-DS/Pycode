# A set is an unordered collection with no duplicate elements
# Basic uses include membership testing and eliminating duplicate entries
# Set object also supports mathematical operations like Union, intersection, difference, symmetrical difference
# Curly braces or the set() function can be used ot create a set
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
#  References for set methods PyDoc - > https://docs.python.org/3/library/stdtypes.html#set

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}

print(basket)  # To demonstrate that duplicates are removed

print("orange" in basket)  #Set membership operation using in

print("crabgrass" in basket)

# Demonstrate set operations on unique letters from two words

a = set("abracadabra")
b = set("alacazam")

print(a)  # This prints unique letters in set a
print(b)  # This prints unique letters in set b

# Set operations in Python
print(a-b)  # print unique letters in a but not in b also termed as difference() operation
# above is equivalent to
print(a.difference(b))


print(a | b)  # print unique letters in a or b or both also termed as Union() operation
# above is equivalent to
print(a.union(b))

print(a & b)  # print unique letters in both a and b also termed as Intersection() operation
# above is equivalent to
print(a.intersection(b))


print(a ^ b)  # print unique letters in a or b but not in both


# Similarly to list comprehensions there is set comprehensions

setcomp = {x for x in "abracadabra" if x not in "abc"}

print(setcomp)

# Creating empty set from Selenium Tutorial With Python by Software Testing Mentor vid - 25
# references - https://www.programiz.com/python-programming/set
# We cannot use {} to create empty set since it is used to create empty dictionary
emp_set = set()

print(emp_set)

# add an element to set using add() function

emp_set.add(1)
print(emp_set)

#Update a datastructure in set
lst =["apple", "mango", "banana"]
emp_set.update(lst)
print(emp_set)

#Discard method in set
emp_set.discard(1)
print(emp_set)

#Other functions on set in python
# Function	Description
# all()	Returns True if all elements of the set are true (or if the set is empty).
# any()	Returns True if any element of the set is true. If the set is empty, returns False.
# enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
# len()	Returns the length (the number of items) in the set.
# max()	Returns the largest item in the set.
# min()	Returns the smallest item in the set.
# sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
# sum()	Returns the sum of all elements in the set.

demo_set1 = {"Delhi", "Kolkata", "Melbourne", "Sydney"}
demo_set2 = {"Delhi", "Kolkata", "Melbourne", "Sydney","New York","Lucknow"}

demo_set3 = demo_set1.union(demo_set2)

print(demo_set3)

demo_set4 = demo_set1.update(demo_set2)  # Update method doesn't return new set as part of its operation.
# it only updates the existing set

print(demo_set4)  # Only returns None since the update method above doesn't return any set as pert of output

#intersection update

demo_set3 = demo_set1.intersection(demo_set2)

print(demo_set3)

demo_set1.intersection_update(demo_set2)  # Similar to update method, but with intersection operation

print(demo_set1)

# Keep all excluding duplicates
demo_set1 = {"Delhi", "Kolkata", "Melbourne", "Sydney"}
demo_set2 = {"Delhi", "Kolkata", "Melbourne", "Sydney", "New York", "Lucknow"}

demo_set3 = demo_set1.symmetric_difference(demo_set2)
print(demo_set3)

demo_set1.symmetric_difference_update(demo_set2)

print(demo_set1)

#Difference and Difference update

demo_set1 = {"Delhi", "Kolkata", "Melbourne", "Sydney"}
demo_set2 = {"Delhi", "Kolkata", "Melbourne", "Sydney", "New York", "Lucknow"}

demo_set3 = demo_set1.difference(demo_set2)
print(demo_set3)

#the below difference is different
demo_set3 = demo_set2.difference(demo_set1)
print(demo_set3)

demo_set2.difference_update(demo_set1)
print(demo_set2)

#issubset and issuperset

demo_set1 = {"Delhi", "Kolkata", "Melbourne", "Sydney"}
demo_set2 = {"Delhi", "Kolkata", "Melbourne", "Sydney", "New York", "Lucknow"}

z= demo_set1.issubset(demo_set2)  # Returns boolean
print(z)

z = demo_set1.issuperset(demo_set2)
print(z)