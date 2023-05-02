# "w" write mode
# "r" read mode
# "a" append mode
# "r+" readand write mode

with open("C:\\Mervin\write2.txt","a") as f:
    f.write("I LOVE PYTHON\n")


with open("C:\\Mervin\write2.txt","r") as f:
    print(f.read())


