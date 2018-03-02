#!/usr/bin/python
"""
author: Bhekimpilo Ndhlela
author: 18998712
module: Applied Mathematics(Numerical Analysis) TW324
task  : computer assignment 01
since : Friday-09-02-2018
"""

#for the square root function and absolute value
from numpy import (sqrt, abs )
def question2(debug=True):
a, b, c = 1.0, -10000.0, 1.0

    xP = (-1*b + sqrt(pow(b,2) - 4*a*c))/ 2*a
    xM = (-1*b - sqrt(pow(b,2) - 4*a*c))/ 2*a

    if debug is True:
        print("x+ = " + str(format(xP, ".20f")))
        print("x- = " + str(format(xM, ".20f")))

    xM2 = c / (a * xP)
    if debug is True:
        print format(xM2, ".20f")

question2()  #call code for question 2
