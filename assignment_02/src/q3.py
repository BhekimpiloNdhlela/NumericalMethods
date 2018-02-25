#!/usr/bin/python

def question_3a(f, debug=True):
    x = [.75, 0, 0, 0, 0, 0]

    for i in xrange(5):
        fx, dx = f(x[i])
        x[i+1] = x[i] - (fx / dx)
        print x[i+1]
        if x[i + 1] is 1.0:
            break

def question_3b(g, debug=True):
    x = [.75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print len(x)
    for i in xrange(38):
        gx, dx = g(x[i])
        x[i+1] = x[i] - (gx / dx)
        print x[i+1]
        if x[i + 1] is 1.0:
            break

def question_3c():
    pass

def question_3d():
    pass

if __name__ == "__main__":

    from numpy import exp
    f = lambda x: (x * exp(x - 1) - 1, exp(x-1) + x * exp(x-1))
    g = lambda x: (-x * exp(1 - x) + 1, -exp(1-x) + x * exp(1-x))

    question_3a(f)
    question_3b(g)
