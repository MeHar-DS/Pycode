print("Addition of 2 and 3: ", 2+3)
print("Subtraction of 2 from 3: ", 3-2)
print("Divide 10 by 5: ", 10/5)  # Classic Division always returns a floating point
print("Divide 5 by 3: ", 5/3)
print("Integer division of 5 by 3: ", 5//3)  # floor division discards the fractional part
print("Remainder of dividing 10 by 4: ", 10%4)  # the % operator returns the remainder of the division
print("Remainder of dividing 5 by 3: ", 5 % 3)
print("50 - 5*6 : ", 50 - 5*6)
print("(50 - 5*6) / 4 : ", (50 - 5*6) / 4)
print("5 * 3 + 2 :", 5 * 3 + 2)  # floored quotient * divisor + remainder
# With Python, it is possible to use the ** operator to calculate powers
print("5 ** 2 :", 5 ** 2)  # 5 squared
# The equal sign (=) is used to assign a value to a variable.
width = 20
height = 5 * 9
print("width * height: ", width * height)
'''There is full support for floating point; 
operators with mixed type operands convert the integer operand to floating point:'''
print("4 * 3.75 - 1 : ", 4 * 3.75 - 1)
'''In interactive mode, the last printed expression is assigned to the variable _. 
This means that when you are using Python as a desk calculator, 
it is somewhat easier to continue calculations'''
'''the _ variable cant be used in pycharm but in interactive python on interpreter'''
tax = 12.5 / 100
print("Tax: ", tax)
price = 100.50
priceintotax = price*tax
print("Price : ", price)
print("price * tax : ", price * tax)
print("round of price * tax :",round(priceintotax, 1))  # 12.6
# Need to explore more on
# Decimal data type
# Fraction datatype
# Complex numbers 3+5j form
