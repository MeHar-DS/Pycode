# Defining functions
def fib(n):  # Write a fibonacci series upto n
    """Print a Fibonacci series upto n."""   # Known as Docstrings
    a, b = 0, 1
    while a<n:
        print(a, end =" ")
        a, b = b, a+b
    print()


fib(10)

# The keyword def introduces a function definition.
# It must be followed by the function name and the parenthesized list of formal parameters.
# The statements that form the body of the function start at the next line, and must be indented.
# The first statement of the function body can optionally be a string literal;
# this string literal is the function’s documentation string, or docstring.
# There are tools which use docstrings to automatically produce online or printed documentation, or
# to let the user interactively browse through code;
# it’s good practice to include docstrings in code that you write, so make a habit of it.
# symbol table- all variable assignments in a function store the value in the local symbol table
# The actual parameters (arguments) to a function call are introduced in the local symbol
# table of the called function when it is called; thus, arguments are passed using call by value
# (where the value is always an object reference, not the value of the object).
# 1 When a function calls another function, or calls itself recursively, a new local symbol table is
# created for that call.
# Every function in python returns a None value unless explicitly it is returning a value

print("Return value of fib() function:", fib(3))


def fib2(n):
    """ Return a list containing Fibonacci series uptil n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print(fib2(10))

# Default arguments
def ask_ok(prompt, retries=4, reminder= "Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries-1
        if retries < 0:
            raise ValueError("Invalid User Response")
        print(reminder)


ask_ok("Do you really want to quit?")


# The default values are evaluated at the point of function definition in the defining scope, so that

i = 5


def f(arg=i):
    print(arg)


i = 6

f()


# The default value is evaluated only once. This makes a difference when the default is a mutable object
# such as a list, dictionary, or instances of most classes.
# For example, the following function accumulates the arguments passed to it on subsequent calls:


def f(a, L = []):
    """ Default values are evaluated only once and at the beginning of the definition"""
    """ Invoking f multiple times  creates accumulation of values rather than assigning unique individual values"""
    L.append(a)
    return L

print(f(1))
print(f(1))
print(f(3))


# If you don’t want the default to be shared between subsequent calls,
# you can write the function like this instead:

def f(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

# def f(a= "StringsOfBeethoven"):
#     print("Value of a: ", a)
#     #return a
#
#
# print(f(1))
# print(f(2))
# print(f(3))