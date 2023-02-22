a = [1, 1, 66.25, 333, 333, 1234.5]
print("a before deleting 0th element", a)
del a[0]
print("a after deleting 0th element", a)

# del to remove slices from a list
del a[1:3]
print("a after deleting slice from 1st element till 2nd element", a)

# clearing an entire list using del
del a[:]
print("a after deleting the entire elements in the list: ", a)

# deleting an entire list object

del a

print(a)  # this throw error since ther is no object a as it was deleted above