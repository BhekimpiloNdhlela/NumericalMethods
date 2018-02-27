#!/usr/bin/python
from numpy import (array, zeros, exp, linalg, negative)
from math import (cos, sin)

def newton_method_sys(fxy, j_0, j_1, debug=True):
    xn = zeros((2, 9))      #store itteration results for x^[n + 1]
    jx = zeros((2, 2))      #store currant itteration jacobian inverse
    fx = zeros((2, 1))      #store the results of the f(x^[n]) for a particular itteration

    sx = zeros((2, 1))

    for i in xrange(len(xn[1]) - 1):
        jx[0][0], jx[0][1] = j_0(xn[0][i], xn[1][i])
        jx[1][0], jx[1][1] = j_1(xn[0][i], xn[1][i])

        fx[0][0], fx[1][0] = fxy(xn[0][i], xn[1][i])
        
        # sx = linalg.lstsq(negative(jx), fx)[3]
	sx = linalg.solve(negative(jx), fx)
        
        xn[0][i + 1] = xn[0][i] + sx[0]
        xn[1][i + 1] = xn[1][i] + sx[1]

    if debug is True:
        # print "\n", "np.linalg.lstsq(jx, Fx)[0] = \n", linalg.lstsq(jx, fx)[0], "\n"
        # print "\n", "np.linalg.lstsq(jx, Fx)[3] = \n", linalg.lstsq(jx, fx)[3], "\n"
        print "Fx = \n", fx, "\n"
        print "jx = \n", jx, "\n"
        print "xn = \n", xn, "\n"

        print "jx[0][0]", jx[0][0], "jx[0][1]", jx[0][1]
        print "jx[1][0]", jx[1][0], "jx[1][1]", jx[1][1]

if __name__ == "__main__":
    fxy = lambda x, y: (x * exp(y) + y - 7, sin(x) - cos(y))    #return a turple
    j_0 = lambda x, y: (exp(y), x * exp(y) + 1)     # 0th row of the jacobian matrix(turple)
    j_1 = lambda x, y: (cos(x), sin(y))             # 1th row of the jacobian matrix(turple)

    newton_method_sys(fxy, j_0, j_1)
