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

def question_c(b=3, a=0, N=0.0, debug=True):
    approx = lambda N : exp(N) * ((b-a)**N / (fact(N) * 2**(2*N-1)))
    while 10**-10 <= approx(N):
        N = N + 1.0

    if debug is True:
        print "\nDEBUG MODE: ON [Question 3 (c.)]:"
        print "Number of Chebyshev Points N = ", int(N)
        print "Approximated Value,      @ N = ", approx(N)
    return N

def question_d(N, debug=True):
    chebyshev_points = zeros(int(N))
    chebyshev_points = [3./2. + 3./2.*cos(((2 * k - 1) * pi)/(2 * N)) \
                        for k in xrange(1, int(N) + 1)]

    if debug is True:
        print "\nDEBUG MODE : ON [Question 3 d.)]"
        print "The n Chebyshev Point where n = ", int(N)
        print "i", "\t", "Chebyshev_Points"
        for i, value in enumerate(chebyshev_points):
            print i, "\t", value


def question_e(debug=True):
    pass

if __name__ == "__main__":
    from math import (cos, pi, exp)
    from numpy import (array, shape, transpose, matmul, zeros)
    from numpy.polynomial import chebyshev as C
    from numpy.linalg import inv
    from scipy.misc import factorial as fact

    x, V = question_a(debug=False)
    question_b(x, V, debug=False)
    N = question_c()
    question_d(N)
    question_e()
else:
    import sys
    sys.exit("Run the library as the client.")
