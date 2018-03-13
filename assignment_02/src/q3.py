#!/usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 02 question 3
since   : Friday-02-03-2018
"""
def question_3a(f, debug=True):
    x = [.9, 0, 0, 0, 0, 0]
    for i in xrange(5):
        fx, dx = f(x[i])
        x[i+1] = x[i] - (fx / dx)

    if debug is True:
        print "Question 3 (a) results:"
        for i in xrange(len(x)):
            print i + 1, "\t", "{:.15f}".format(x[i])

def question_3b(g, debug=True):
    x = [.9, 0, 0, 0, 0, 0]
    for i in xrange(5):
        gx, dx = g(x[i])
        x[i+1] = x[i] - (gx / dx)

    if debug is True:
        print "Question 3 (b) results:"
        for i in xrange(0 ,len(x)):
            print i + 1, "\t", "{:.15f}".format(x[i])

def question_3d(g, debug=True):
    x = [.9, 0, 0, 0, 0, 0]
    # m == multiplicity of the function g(x)
    m = 2
    for i in xrange(5):
        gx, dx = g(x[i])
        x[i+1] = x[i] - (m * (gx / dx))

    if debug is True:
        print "Question 3 (d) results:"
        for i in xrange(0 ,len(x)):
            print i + 1, "\t", "{:.15f}".format(x[i])

if __name__ == "__main__":
    from numpy import exp
    f = lambda x: (x * exp(x - 1) - 1, exp(x-1) + x * exp(x-1))
    g = lambda x: (-x * exp(1 - x) + 1, -exp(1-x) + x * exp(1-x))

    question_3a(f)
    question_3b(g)
    # no code required for 3 (c)
    question_3d(g)
else:
    import sys
    sys.exit("please run as client...")
