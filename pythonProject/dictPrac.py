# dictionary is ordered changeable and does not allow duplicates

s = {"Name": "Vaulkswagen", "Brand": "Polo", "Year": "2000"}

print(s, type(s))

# print(s.keys())
# print(s.values())
# print(s)

for k in s:
    print("The value of {} is {}".format(k,s[k]))

for k in s.keys():
    print(k)

for v in s.values():
    print(v)

c= s.copy()

print(c)

c["Name"] =" Merc"

print(c)
print(s)