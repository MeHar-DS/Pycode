# When looping trough dictionaries we can extract the corresponding key and value using the items() method

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)

# when looping thorough a sequence, the position index and the corresponding value can retrieved at the same
# time using the enumerate() function

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# to loop over two or more sequences at the same time, the entries can be paired with the zip() function
# zip function takes iterables as input

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the Holy Grail', 'blue']

for q, a in zip(questions, answers):
    print("What is your names {0}? it is {1}".format(q, a))


# To loop over a sequence in reverse, first specify the sequence in a forward direction
# and then call the reversed() function

for i in reversed(range(1, 10, 2)):
    print(i)


# To loop over a sequence in sorted order use the sorted() function

basket = ['apple','orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket, reverse=True):
    print(i)


# Using set() on a sequence eliminates duplicate elements.
# The use of sorted() in combination with set() over a sequence is an idiomatic way to loop
# over unique elements of the sequence in sorted order

for f in sorted(set(basket)):
    print(f)


# It is sometimes tempting to change a list while you are looping over it; however,
# it is often simpler and safer to create a new list instead

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)


# while loop

x = 0
while x <= 10:
    print(x)
    x += 1

city = "Melbourne"
x = 0
while x < len(city):
    print(city[x])
    x += 1


city = ["Mumbai", "NewYork", "London"]
country = ["India","USA","UK"]
buffer = [1, 2, 3]

s = zip(city, country, buffer)

print(s)
print(list(s))

for x, y in zip(city, country):
    print(x, y)

cost = [46,6,7,89,90]
saleprice = [50,10,2,80,100]

for x, y in zip(cost,saleprice):
    print(y-x)


cities =[["Mumbai", "India"], ["Vancouver", "Canada"], ["Newyourk", "USA"], ["London","UK"]]

for x, y in cities:
    print("City is ", x ,"in the country ", y)

# iterating over sets
fruits = {"apples","mangoes","bananas", "strawberrie"}

for x in fruits:
    print(x)

# Iterating over dictionaries

dict_cities = dict(cities)

for city, country in dict_cities.items():
    print(city,country)
    for s in city:
        print(s)


