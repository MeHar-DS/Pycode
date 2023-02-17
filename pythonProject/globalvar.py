x = "awesome"
#
#
# def myfunc():
#     x = "fantastic"
#     print(x,"from myfunc")
#
#
# myfunc()
#
# print("Python is {}".format(x))


# To create a global variable inside a function

def myfunc():
    global x
    x = "globally"
    print(x)

myfunc()

print("from outside the value of x is :", x)

# We can use the global keyword to change the value of a global variable inside a function


