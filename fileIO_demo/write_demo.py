# "w" write mode
# "r" read mode
# "a" append mode
# "r+" readand write mode

# f = open("writefile.txt","w")
# f = open("C:\\Mervin\\funny.txt","r")
# f.write("This is a write demo using the file methods")
# f.close()

l = [1,2,3,4,5,6,7,8]
f = open("C:\\Mervin\\write2.txt","w")

for items in l:
    f.write(str(items)+"\n")

f.close()