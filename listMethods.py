fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

newFruits = ["Strawberry", "Litchi", "Musk Melon"]
print(fruits.count("apple"))
print(fruits.count("tangerine"))
print(fruits.index("banana", 4))  # Find next banana starting at 4
fruits.insert(len(fruits), "Passion Fruit")
fruits.extend(newFruits)

# Extend adds the content of the list
# Append just adds the new data structure into the list.
# Say, a list is appended then the resultant list will have original contents plus a new list within

#fruits.append(newFruits)
print(fruits)
print("Reverse: ", fruits.reverse())
print(fruits)

print("Append:", fruits.append("grape"))
# print(fruits)

print("Sort: ", fruits.sort())
print(fruits)

print(fruits.pop())

fruits.remove("grape")
print(fruits)

newFruits.clear()

fruits.append(newFruits)  # This adds an empty list

# fruits.sort()  # Error - You cannot sort if the list contains a list

print(fruits)

copyList= fruits.copy()

print("This is the copied list of fruits using shallow copy method: ", copyList)

# You might have noticed that methods like insert, remove or sort that only modify the list
# have no return value printed – they return the default None.
# This is a design principle for all mutable data structures in Python



