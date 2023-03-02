# Sequence objects types may be compared to other objects with same sequence types
# The comparison uses lexicographic ordering: first the first two items are compared
# And if they differ then this determines the outcome of the comparison;
# If they are equal, the next two items are compared, and so on, until the sequence is exhausted
# If all items of two sequence type compare equal then the sequence is considered equal

print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])

print('ABC' < 'C' < 'Pascal' < 'Python')

print((1, 2, 3, 4) < (1, 2, 3))

print((1, 2) < (1, 2, -1))

print((1, 2, 3) == (1.0, 2.0, 3.0))

print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))



