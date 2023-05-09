# "w" write mode
# "r" read mode
# "a" append mode
# "r+" read and write mode

with open("C:\\Mervin\write2.txt","a", encoding= 'utf-8') as f:
    f.write("I LOVE PYTHON\n")


with open("C:\\Mervin\write2.txt","a", encoding= 'utf-8') as f:
    f.write("Checking whether this appends..")
    f.write("Next step is to clean all the contents..")


with open("C:\\Mervin\write2.txt","r", encoding= 'utf-8') as f:
    print(f.read())

with open("C:\\Mervin\write2.txt","w", encoding= 'utf-8') as f:
    f.write("")  # To clean the contents of the file