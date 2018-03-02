#!/usr/bin/python

"""
author: Bhekimpilo Ndhlela
author: 18998712
module: Applied Mathematics(Numerical Analysis) TW324
task  : computer assignment 01
since : Friday-09-02-2018
"""

def question1a():
    step, x = 1./10,1.0
    print "=" * 64
    for i in xrange(0,10):
        E1 = (1-cos(x)) / pow(sin(x),2)
        E2 = 1 / ( 1 + cos(x))
        print( format(x, ".14f") + "\t" + format(E1, ".14f") + "\t" + format(E2, ".14f"))
        x = x * step
    print "=" * 64

def question1b():
    print "=" * 64
    step, x = 1./10,1.0
    for i in xrange(0,10):
        F1 = ((1-1/cos(x))/ pow(sin(x)/cos(x),2))
        F2 = -1*(cos(x) / ( 1 + cos(x)))
        print( format(x, ".14f") + "\t" + format(F1, ".14f") + "\t" + format(F2, ".14f"))
        x = x * step
    print "=" * 64

from math import (cos, sin)
question1a() #call code for question 1a
question1b() #call code for question 1b
