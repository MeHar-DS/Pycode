# discussed in Selenium Python Tutorial Vid 41

demo_tuple =(5,7,8,2,3,4,4,3,8)
x= max(demo_tuple)  # returns largest items in iterable - tuple-list-string, dictionary set
y = min(demo_tuple)  # returns smallest items in iterable - tuple-list-string, dictionary set
print(x)

i = iter(demo_tuple)  # to iterate the items in an iterable - returns an iterator object
j = reversed(demo_tuple)  # Iterates by reversing the order of the iterable returns a reversed iterator

print(next(i))
print(next(j))
print(next(i))
print(next(j))

a = slice(2,5)  #Retruns a slice object
b = slice(2,5,2)  # Step of 2 is the 3rd parameter
print(demo_tuple[a])
print(demo_tuple[b])

z = sorted(demo_tuple)  # Returns a sorted list

print(z)

zz = sum(demo_tuple)   #Sums the items of the iterator
yy = sum(demo_tuple,5)  # Variant of sum where 5 is added to the sum result
print(zz)
print(yy)

ee = input("Enter your name")
print("Welcome "+ee)
