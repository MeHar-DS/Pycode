x = int(input("Please enter an integer"))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("zero")
elif x == 1:
    print("Single")
else:
    print("More")

# iterating over a list of items and modifying them as we traverse using the copy() function

fruits=["apple", "orange", "peach", "litchi"]

for f in fruits.copy():
    if f == "apple":
        print(fruits.index(f))

# code using a collection

users= {"Ron" : "Active", "Jon" : "Inactive", "Chris" : "On Hold", "Don" : "Suspended"}

for user,stat in users.copy().items():

    if stat == "Suspended":
        del users[user]
print(users)

print(range(0,10))

a=300
b=200

if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a and b are equal")

print("a greater than b") if a>b else print("b greater than a")

i = 1
for i in "Stringval":
    print(i)

