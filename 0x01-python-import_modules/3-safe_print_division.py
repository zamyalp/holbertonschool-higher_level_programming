#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division
a = 12
b = 2
try:
div=num1/num2;
except:
    print("The division of {0} and {1} is: none".format(num1,num2))
finally:
    print("The division of {0} and {1} is: {2}".format(num1,num2,div))
