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

def question2(debug=False):
    a, b, c = 1.0, -10000.0, 1.0

    xP = (-1*b + sqrt(pow(b,2) - 4*a*c))/ 2*a
    xM = (-1*b - sqrt(pow(b,2) - 4*a*c))/ 2*a

    if debug is True:
        print("x+ = " + str(format(xP, ".20f")))
        print("x- = " + str(format(xM, ".20f")))

    xM2 = c / (a * xP)

    if debug is True:
        print format(xM2, ".20f")

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
    """
    this is the helper function for finding the approximations of J[n](x)
    """
    J = 0
    for k in xrange(0, 4): # "4" is exclusive
        #N = numerator
        N = pow(-1, k) * pow(float(x)/2, n + (2 * k))
        #D = Denominator
        D = sm.factorial(k) * sm.factorial(n + k)
        J = J + (N / D)
    return J
     
def question3b(x=1, debug=False):

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

def question3c():
    pass

if __name__ == "__main__":
    """
    The main function that calls the functions or better of 
    the client library.
    """
    #for both cosine and sine functions
    from math import (cos, sin)
    #for the square root function
    from numpy import (sqrt, abs )
    #import this for scipy special jn
    import scipy.special as ss
    #import this for scipy misc factorial [for efficient factorial]
    import scipy.misc as sm 


    #question1a() #call code for question 1a
    #question1b() #call code for question 1b
    question2()  #call code for question 2

    question3a()  #call code for question 3a
    question3b()  #call code for question 3b
    question3c()  #call code for question 3c
else: pass
