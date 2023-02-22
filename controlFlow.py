users ={'Hans': 'active', 'Eleonore': 'inactive', 'chen': 'active' }

# for user,status in users.copy().items():
#     print(user, status)


for user,status in users.copy().items():
    if status == 'inactive':
        del users[user]

# strategy create a new collection

active_users ={}

for user,status in users.items():
    if status == 'active':
        active_users[user]= status

# range() function
# range is a function that returns an object which stores a sequence of items
# such object is called iterable that is, sutiabel for functions or constructs that
# expect something from which they can obtain successive items until supply is exhausted
# for is such a function and so is sum()

print("Sum is :", sum(range(6)))




for i in range(10):
    print(i)

for u in range(2,10,1):
    print(u , end=".")

l1= list(range(1,10))
print(l1)

l2= list(range(0,10,3))
print(l2)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))

print(list(range(2,2)))



for n in range(2, 10):
    print("n is: ", n)
    for x in range(2, n):
        print("x is: ", x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# pass statement is used when you dont want the code to do anything. it simply doesnt do anything
# Can be used when u are developing code in the initial stages before a concrete code is written
# allowing you to keep thinking at a more abstract level
# The pass is silently ignored
class MyEmptyClass:
    pass