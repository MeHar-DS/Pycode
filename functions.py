# Empty functions can be written as belo- helps in creating a template

def add():
    pass


# Addition function

def add(x,y):
    print(x+y)


# return statement

def addreturn(x,y):
    """
    this is a docstirng- best practice to describe the function
    """
    return x+y


z = addreturn(1,2)

print(z)
print(addreturn(102, 2030))

# Positional Arguments
def addreturn(x,y):
    """
    this is a docstirng- best practice to describe the function
    """
    return x+y
print(addreturn(1,2))  # Positional Arguments

# Keyword arguments
def addreturn(x=0,y=0):
    """
    this is a docstirng- best practice to describe the function
    """
    return x+y


print(addreturn(x=1,y=2))  # Keyword arguments
print(addreturn(y=1))  # Keyword arguments
print(addreturn(x=1))  # Keyword arguments

print(addreturn()) # optional arguments- since default are provided in addreturn() on line 36



