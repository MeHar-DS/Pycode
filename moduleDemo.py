# A python script is a collection of functions or variables of definitions of python codes
# This script can be executed by running it as an input in the interpreter
# It helps to maintain if your code grows. We may also want to use a handy function that can be
# used in multiple program files
# To support this python has a way to put definitions in a file and use them as a script
# or in an interactive instance of the interpreter.
# Such a file is called as a module.
# Definitions from a module can be imported in a different module or main module
# A module is a file containing Python definitions and statements.
# The file name is the module name with the .py suffix in this instance moduleDemo.py
# Fibonacci numbers module

def fib(n):  # Write Fibonacci series upto n
    a, b = 0, 1
    while a<n:
        print(a, end =' ')
        a, b = b, a+b
    print()


def fib2(n):  # Write Fibonacci series upto n
    result = []
    a, b =0, 1
    while a < n:
        result.append(a)
        a, b =b,a+b
    return result


print("Module name  : ", __name__)   # Prints __main__


# With import all the modules names are included in the calling module
# The variant of import that selectively includes the names is as below:
# from module-name import function1, function2.. functon N OR
# from module-name import * (all the functions and codes names except those beginning with underscores)

# if the module name is followed by "as", then the name following "as" is bound directly to the imported module

# import "module-name" as "alias"
# It can also be written with from form as below:
# from "module-name" import "function-name" as "alias"

# For efficiency reasons, each module is only imported once per interpreter session.
# Therefore, if you change your modules, you must restart the interpreter – or,
# if it’s just one module you want to test interactively,
# use importlib.reload(), e.g. import importlib; importlib.reload(modulename).

# Executing modules as script
# When a python module is run as below:

# python moduleDemo.py <arguments>

# the code in the module will be executed just as if you imported it with the __name__ = '__main__'. That means
#adding the below code at the end of your module

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))

# You cna make the code re-usable as an executable script as well as to be imported as a module

# python moduleDemo.py 50   # this runs the module with the method


# if the module is imported as below then the code is not run

# This is often used to either provide a convenient user-interface to a module
# or for testing purposes( running the module as a script executes as a test suite)

