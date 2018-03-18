#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : Computer Assignment 03 question 3 (a. to e.)
since   : Friday-09-03-2018
"""

def questiona(debug=True):
    """

    write down the documentation of this question here

    """
    N = 4  #4 points from the chebyshev points
    x = array([0.0, 0.0, 0.0, 0.0])
    x.shape = (4, 1)
    x = [cos(((2 * k - 1) * pi)/(2 * N)) for k in xrange(1, N + 1)]

    # defining the chebyshev Vandermonde matrix where V = 4x4 Matrix
    V = C.chebvander(x, N - 1).T

    if debug is True:
        print "DEBUG MODE: ON [Question 3 (a.)]:"
        print "vector x   = ", x
        print "\nchebyshev Vandermonde matrix where V:      \n", V

    return x, V

def questionb(x, V, debug=True):
    # finding the e^xi for the x elements
    exp_x = [exp(i) for i in x]
    V_inv = inv(V)
    c = matmul(exp_x, V_inv)

    if debug is True:
        print "\nDEBUG MODE: ON [Question 3 (b.)]:"
        print "vector e^x = ", exp_x
        print "\n(chebyshev Vandermonde matrix)^-I where V :\n", V_inv
        print "\nVc=exp(x)=> c=inv(V)exp(c) <=> inv(V)V=I  :\n", c

def questionc(debug=True):
    """
        Use the inequality on slide 10 of Lecture 13 to
        estimate how many Chebyshev points, x 1 , . . . , x n ,
        will be necessary to approximate the function
        exp(x) to an accuracy of 10e−10 on the interval [0, 3].
    """
    pass

if __name__ == "__main__":
    from math import (cos, pi, exp)
    from numpy import (array, shape, transpose, matmul)
    from numpy.polynomial import chebyshev as C
    from numpy.linalg import inv
    x, V = questiona()
    questionb(x, V)
else:
    import sys
    sys.exit("Run the library as the client.")
