# Demo of match expression with pattern
# Python 3.9 does not support match statements
def httpstatus(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I am a Teapot"
        case _:  # variable name _ is the wildcard character and never fails to match
            return "Something's wrong with the internet"

httpstatus(700)

# patterns can also be combined by an OR condition using the | symbol

# case 400|403|404:
#     return "Not Allowed"

# Patterns can alos look like unpacking assignments
# point is an (x, y) tuple
match point:
    case (0,0):
        print("Origin")
    case (0,y):
        print(f"Y = {y}")
    case (x,0):
        print(f"X = {x}")
    case (x,y):
        print(f"X = {x}, Y = {y}")
    case _:
        raise ValueError("Not a Point")

# The first pattern has two literals, and can be thought of as an extension of the literal pattern shown above.
# But the next two patterns combine a literal and a variable, and the variable binds a value from the subject (point).
# The fourth pattern captures two values, which makes it conceptually similar to the unpacking assignment (x, y) = point

# If you are using classes to structure your data you can use the class name followed by an argument
# list resembling a constructor, but with the ability to capture attributes into variables:

class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

# A recommended way to read patterns is to look at them as an extended form of what you would put on the
# left of an assignment, to understand which variables would be set to what.
# Only the standalone names (like var above) are assigned to by a match statement.
# Dotted names (like foo.bar), attribute names (the x= and y= above) or class names
#     (recognized by the “(…)” next to them like Point above) are never assigned to.

# Patterns can be arbitrarily nested. For example, if we have a short list of points,
# we could match it like this:

match points:
    case []:
        print("No Points")
    case [Point(0,0)]:
        print("Origin")
    case [Point(x,y)]:
        print(f"single point {x},{y}")
    case [Point(0,y1), Point(0,y2)]:
        print(f"Two on the Y-axis at {y1}, {y2}")
    case _:
        print("Something Else")

# We can add an if clause to a pattern, known as a “guard”. If the guard is false,
# match goes on to try the next case block.
# Note that value capture happens before the guard is evaluated

match Point:
    case Point(x,y) if x==y:
        print(f"Y=X at {X}")
    case Point(x,y):
        print("Not on diagonal")

