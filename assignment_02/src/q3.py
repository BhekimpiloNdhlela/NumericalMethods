#!/usr/bin/python
def question_3a(f, debug=True):
    x = [.9, 0, 0, 0, 0, 0]
    for i in xrange(5):
        fx, dx = f(x[i])
        x[i+1] = x[i] - (fx / dx)

    if debug is True:
        print "Question 3 (a) results:"
        for i in xrange(len(x)):
            print i, "\t", x[i]

def question_3b(g, debug=True):
    x = [.9, 0, 0, 0, 0, 0]
    for i in xrange(5):
        gx, dx = g(x[i])
        x[i+1] = x[i] - (gx / dx)
    if debug is True:
        print "Question 3 (b) results:"
        for i in xrange(0 ,len(x)):
            print i, "\t", x[i]
    """
    osbevation: question_3b will never equal to one even if the number of
    iterations is increased to 100. However, it approches 1.0 as the number
    of itterations increase
    """

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
            print i, "\t", x[i]

if __name__ == "__main__":
    from numpy import exp
    f = lambda x: (x * exp(x - 1) - 1, exp(x-1) + x * exp(x-1))
    g = lambda x: (-x * exp(1 - x) + 1, -exp(1-x) + x * exp(1-x))

    question_3a(f)
    question_3b(g)
    # no code required for 3 (c)
    question_3d(g)
