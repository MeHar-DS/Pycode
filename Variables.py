import keyword
lst_keywrd = keyword.kwlist
print("list of keywords :",lst_keywrd) #These cannot be used as variable names
print("Is a keyword?:", keyword.iskeyword("try"))

#Variables
#integer
x=1
print(type(x))
#float
x=9.1
print(type(x))
print("x: ",x)
#string
x="Mervin"
print(type(x))
#casting
#y= int(x)
#print(y)

# from Selenium Python Tutorial - vid 12
# id function gives the address of the variable
print(id(x))


# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
# invalid and valid variable names in python

#Valid one-
my_var =1
_my8_var = "twelve"
MYVAR = 1.0  # Different from myvar
print(my_var,_my8_var, MYVAR)

#Invalid variable names

# 1_my8_var = True
#%my_var = 1+3i
#my-var = 2.2
# test_var_&*@ = "This is testvar"

#print(1_my8_var, %my_var, my-var, test_var_&*@ )
