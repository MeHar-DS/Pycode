# The conditions used in "While" and "if" statements can contain any operators not just comparisons
# The comparison operators "in" and "not in" are membership tests that determine whether a value is in (or not in)
# a container
# The operator "is" and "is not" compare whether two objects are really the same object
# Comparisons can be chained a < b == c tests whether a is less than b and b is equal to c
# Comparisons may be combined using Boolean operators "and" & "or" and the outcome of a comparison may be
# negated with "not"
# These have lower priorities than comparison operators; between them "not" has the highest priority and "or"
# the lowest.
# Parentheses can be used to achieve the desired combination
# The Boolean operators "and" "or" are called "short-circuit" operators and evaluated from left to right
# The evaluation stops when an expression outcome is evaluated

# It is possible to assign the result of a condition or a Boolean expression to a variable
string1, string2, string3 = "", "Trondheim", "Hammer Dance"
non_null = string1 or string2 or string3

print(non_null)
