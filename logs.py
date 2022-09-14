# logs.py
#
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

import math

def g(x):
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

x = input("Input the value for x: ")
x = float(x)

if x < -9:
    print("Number to low, please input higher value")  

elif x >= 8:
    print("Number to high, please input lower value")
    
else:
    print("g(" + str(x) + ") = " + str(g(x)))
