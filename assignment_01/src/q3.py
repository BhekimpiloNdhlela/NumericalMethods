#!/usr/bin/python
"""
author: Bhekimpilo Ndhlela
author: 18998712
module: Applied Mathematics(Numerical Analysis) TW324
task  : computer assignment 01
since : Friday-09-02-2018
"""

def question3a(debug=False):
    # get approximation values [J0, J1] respectively
    J0 = get_appr3A(0)
    J1 = get_appr3A(1)

    #get built in values for [J0, J1] respectively
    blt_val0 = ss.jn(0, 1)
    blt_val1 = ss.jn(1, 1)

    #get absolute error [abs_err0, abs_err1] respectively
    abs_err0 = abs(J0 - blt_val0)
    abs_err1 = abs(J1 - blt_val1)

    if debug is True:
        print "(appro_val0, blt_val0, abs_err0) = (" + str(J0) + ", " + str(blt_val0) + ", " + str(abs_err1)+")"
        print "(appro_val1, blt_val1, abs_err1) = (" + str(J1) + ", " + str(blt_val1) + ", " + str(abs_err1)+")"

def get_appr3A(n, x=1):
    J = 0
    for k in xrange(0, 4): # "4" is exclusive
        N = pow(-1, k) * pow(float(x)/2, n + (2 * k))
        D = sm.factorial(k) * sm.factorial(n + k)
        J = J + (N / D)
    return J

def question3b(x=1, debug=True):
    vector_J_A = []     #vector to store approximations
    vector_J_B = []     #vector to store built in value
    vector_J_A.append(get_appr3A(0))
    vector_J_A.append(get_appr3A(1))

    for n in xrange(1, 7):
        vector_J_A.append((((2 * n) / x) * vector_J_A[n]) - vector_J_A[n - 1])
    for n in xrange(0, 8):
        vector_J_B.append(ss.jn(n, 1))

    print len(vector_J_A), len(vector_J_B)
    if debug is True:
        print vector_J_A
        print vector_J_B

import scipy.special as ss
#import this for scipy misc factorial [for efficient factorial]
import scipy.misc as sm

question3a()
question3b()
