#!/usr/bin/python
def newton_method_sys(fxy, j0, j1, debug=True):
    xn = zeros((2, 9))      #store itteration results for x^[n + 1]
    jx = zeros((2, 2))      #store currant itteration jacobian inverse
    fx = zeros((2, 1))      #store the results of the f(x^[n]) for a particular itteration
    sx = zeros((2, 1))

    for i in xrange(len(xn[1]) - 1):
        jx[0][0], jx[0][1] = j0(xn[0][i], xn[1][i])
        jx[1][0], jx[1][1] = j1(xn[0][i], xn[1][i])
        fx[0][0], fx[1][0] = fxy(xn[0][i], xn[1][i])
        sx = linalg.solve(negative(jx), fx)
        xn[0][i + 1] = xn[0][i] + sx[0]
        xn[1][i + 1] = xn[1][i] + sx[1]

    if debug is True:
        print "xn = |", xn[0][-1], xn[1][-1], "|"

if __name__ == "__main__":
    from numpy import (array, zeros, exp, linalg, negative)
    from math import (cos, sin)
    fxy = lambda x, y: (x * exp(y) + y - 7, sin(x) - cos(y))
    j0 = lambda x, y: (exp(y), x * exp(y) + 1)
    j1 = lambda x, y: (cos(x), sin(y))
    newton_method_sys(fxy, j0, j1)
