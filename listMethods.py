fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print(fruits.count("apple"))
print(fruits.count("tangerine"))
print(fruits.index("banana", 4))  # Find next banana starting at 4

print("Reverse: ", fruits.reverse())
print(fruits)

print("Append:", fruits.append("grape"))
#print(fruits)

print("Sort: ", fruits.sort())
print(fruits)

print(fruits.pop())

print(fruits)


# You might have noticed that methods like insert, remove or sort that only modify the list
# have no return value printed – they return the default None.
# This is a design principle for all mutable data structures in Python


# Using lists as stacks
