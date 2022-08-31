#!/usr/bin/python3
def safe_print_division(a, b):
try:
    div=a/b
except:
    print("The division of {0} and {1} is: none".format(a,b))
finally:
    print("The division of {0} and {1} is: {2}".format(a,b,div))
