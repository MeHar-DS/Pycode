# Tuple is a sequence type similar to lists and strings

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


