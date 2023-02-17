# fibonacci series
# Demo of multiple assignments

a,b=0,1
for i in range (10):
    a,b=b,a+b
    print(a)

# Similar program implemented with while loop

a,b=0,1

while a<90:
    a,b = b,a+b
    print(a, end =',')
# end is a keyword to stop the newline defaulted by print

#taking user input
val = int(input("Enter the number to be squared"))
def squaring (val):
    return val*val

print("Square of {}".format(val), squaring(val))

