# Dictionaries are indexed by keys, which can be any immutable type; do not allow duplicates
# strings and numbers can always be keys.
# Tuples can be used as keys if they contain only strings, numbers, or tuples;
# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
# You can’t use lists as keys, since lists can be modified in place using
# index assignments, slice assignments, or methods like append() and extend()

# It is best to think of dictionaries as Key value pairs with the requirement that
# keys are unique within one dictionary
# A pair of braces creates an empty dictionary {}

# The main operations for a dictionary are storing a value with some key and extracting the value given the key
# It is also possible to delete a key value pair with the del
# If you store a value with an already existing key then the old value is replaced
# It is an error to extract a non-existing key

# Performing list(d) on a dictionary creates a list with the keys used in the dictionary, in insertion order
# If you want the list to be sorted then sorted(d) can be used
# To check whether a key is existing in dictionary use the in keyword

emp_dict = {}  # Empty dictionary defined

tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']

print(tel)

tel['irv'] = 4127

print(tel)

print(list(tel))  # This prints the list of keys in the inserted order

print(sorted(tel))

print("guido" in tel)

print("jack" not in tel)


# The dict() constructor builds dictionaries directly from sequences of key-value pairs

dictfromseq = dict([('sape', 4139),('guido',4127), ('jack', 4098)])

print(dictfromseq)

# Dictionary comprehensions can be used to create dictionaries from arbitrary key and value expressions

dictcomp = {x: x**2 for x in range(1, 10)}

print(dictcomp)


# When the keys are simple strings it is sometimes easier to specify pairs using keyword arguments

dictstrings = dict(John=1111, Don=2222, Sam=3333)

print(dictstrings)


demo_dict ={1:10, 2: 20, 3:30, 4:40, 5:50}
demo_dict2= {"qa": "testurl", "uat":"uaturl"}
demo_dict3= {'qa':1, 3:"uaturl"}

print(demo_dict2["uat"])  # prints uaturl
print(demo_dict3[3])  # Prints uaturl

#Adding items to dictionary

print("prior adding to demo_dict2:", demo_dict2)

demo_dict2['prod'] = "produrl"

print("after adding prod to demo_dict2",demo_dict2)



print("after removing or popping the prod", demo_dict2)

# methods of dictionary

print(demo_dict2.get("qa"))
print(demo_dict2.keys())
print(demo_dict2.values())
print(demo_dict2.items())  # The returned list contains tuples of all the key:value pairs in the dictionary

# removing the item from dictionary
print(demo_dict2)
demo_dict2.pop("qa")
print(demo_dict2)
demo_dict2.popitem()  # removes the last item
print(demo_dict2)

demo_dict2.update({"prod":"produrl", "uat":"uaturl", "qa":"qaurl"})

print(demo_dict2)

demo_dict_copy = demo_dict2.copy()

print(demo_dict_copy)

demo_dict_copy.clear()  # clears all items

print(demo_dict_copy)