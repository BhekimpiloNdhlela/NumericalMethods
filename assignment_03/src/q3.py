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
    else:
        print "\nDEBUG MODE : OFF [Question 3 d.)]"
    return chebyshev_points

def question_e(chebyshev_points, debug=True):
    exp_xk = [exp(vk) for vk in chebyshev_points]
    #use polyfit
    fit = polyfit(chebyshev_points, exp_xk, len(exp_xk) - 1)
    err_vals = [e - f for e, f in zip(exp_xk, fit)]
    warnings.simplefilter('ignore', RankWarning) #ignore warnings
    # plot the error function
    plt.plot(linspace(0,3,num=19), exp_xk, label="exp(xk)")
    plt.plot(linspace(0,3,num=19), err_vals, label="err_vals")
    plt.plot(linspace(0,3,num=19), fit, label="fit")
    plt.legend(bbox_to_anchor=(1.0, 1), loc=0, borderaxespad=0.)
    plt.show()

    if debug is True:
        print "\nDEBUG MODE : ON  [Question 3 e.)]"
        print "k", "\t", "chebyshev_points(k)", "\t", "exp(k)\t\t\t", "polyfit_points(k)"
        for k, (xk, e) in enumerate(zip(chebyshev_points, exp_xk)):
            print k, "\t", "{:.16f}".format(xk), "\t","{:.16f}".format(e), \
                  "\t", "{:.16f}".format(fit[k])
    else:
        print "\nDEBUG MODE : OFF [Question 3 e.)]"

if __name__ == "__main__":
    from math import (cos, pi, exp)
    from numpy import (array, shape, transpose, matmul, zeros, polyfit, RankWarning)
    from numpy.polynomial import chebyshev as C
    from numpy.linalg import inv
    from scipy.misc import factorial as fact
    import warnings
    import matplotlib.pyplot as plt
    from numpy import linspace


    x, V = question_a(debug=True)
    question_b(x, V, debug=True)
    N = question_c()
    chebyshev_points = question_d(N)
    question_e(chebyshev_points)
else:
    import sys
    sys.exit("Run the library as the client.")
