# Tuple is a sequence type similar to lists and strings
# Tuples are indexed, immutable, allow duplicates

t = 12345, 54321, "Hello!"

print(t)

# Tuple is immutable - it is not possible to assign values individually

# t[0] = 99  # Error- Impossible to assign values to tuple

# Although tuples are immutable, it is possible to create tuples using mutable objects such as lists
# Tuples can contain heterogeneous elements , however, lists are usually homogeneous
# To construct tuple with zero elements

t0 = ()
print("Type of variable t : ", type(t0), "and its length :", len(t0))

# To construct tuple with 1 element

t1= "hello",

print(t1, " and its type", type(t1),"and its length is :", len(t1))

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing:
# the values 12345, 54321 and 'hello!' are packed together in a tuple.
# The reverse operation is also possible: It is called unpacking

x, y, z = t

# Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.


demo_tuple = (1,2,3,4,5)
print(demo_tuple[1])

demo_tuple2 = ("Delhi", "Mumbai", "NewYork", "Melbourne", "Sydney", "Delhi")  # Allows duplicates

demo_tuple3 = (True, False, False, True)  # Boolean value Tuple

demo_tuple4 = (True, 1, "False", 2.5)

# print(demo_tuple4.append())  # Append Not available and cannot be performed since immutable

# print(demo_tuple4.pop())  # Pop Not available and cannot be performed since immutable

print(len(demo_tuple4))

print(demo_tuple2.count("Delhi"))

joined_tuple = demo_tuple+demo_tuple2+demo_tuple3+demo_tuple4  # Joining tuples

print(joined_tuple)

print(joined_tuple[3:5])



print(demo_tuple2.index("Delhi"))