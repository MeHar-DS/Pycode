# "w" write mode
# "r" read mode
# "a" append mode
# "r+" readand write mode

f = open("C:\\Mervin\\funny.txt","r")
#print(f.read())

# Reads first line
print(f.readline())

# Read second line
print(f.readline())

# Now opening the above file and writing a line via the write() method
f = open("C:\\Mervin\\funny.txt","a")
f.write("This is a next line written from py code write() method\n")

f = open("C:\\Mervin\\funny.txt","r")  # In append mode we cannot read a file
print(f.read())
f.close()
