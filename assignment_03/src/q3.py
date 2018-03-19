#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : Computer Assignment 03 question 3 (a. to e.)
since   : Friday-09-03-2018
"""

def question_a(N=4, debug=True):
    x = zeros(N)
    x = [cos(((2 * k - 1) * pi)/(2 * N)) for k in xrange(1, N + 1)]
    # defining the chebyshev Vandermonde matrix where V = 4x4 Matrix
    V = C.chebvander(x, N - 1).T

    if debug is True:
        print "DEBUG MODE: ON [Question 3 (a.)]:"
        print "vector x   = ", x
        print "\nchebyshev Vandermonde matrix where V:      \n", V
    return x, V

def question_b(x, V, debug=True):
    # finding the e^xi for the x elements
    exp_x = [exp(i) for i in x]
    V_inv = inv(V)
    c = matmul(V_inv, exp_x)

    if debug is True:
        print "\nDEBUG MODE: ON [Question 3 (b.)]:"
        print "vector e^x = ", exp_x
        print "\n(chebyshev Vandermonde matrix)^-I where V :\n", V_inv
        print "\nVc=exp(x)=> c=inv(V)exp(c) <=> inv(V)V=I  :\n", c

def question_c(debug=True):
    pass

def question_d(N=4, debug=True):
    chebyshev_points = zeros(N)
    chebyshev_points = [cos(((2 * k - 1) * pi)/(2 * N)) for k in xrange(1, N + 1)]

    if debug is True:
        print "DEBUG MODE : ON [Question 3 d.)]"
        print "The n Chebyshev Point where n = ", N, "are:\n", chebyshev_points

def question_e(debug=True):
    pass

if __name__ == "__main__":
    from math import (cos, pi, exp)
    from numpy import (array, shape, transpose, matmul, zeros)
    from numpy.polynomial import chebyshev as C
    from numpy.linalg import inv
    x, V = question_a(debug=False)
    question_b(x, V, debug=False)
    question_d(debug=False)
    question_e()
else:
    import sys
    sys.exit("Run the library as the client.")
