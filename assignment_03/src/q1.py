#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 03 question 1 (a. to d.)
since   : Friday-09-03-2018
"""
def question_a(debug=True):
    global J
    J = [bessel_function(i) for i in xrange(0, 4)]
    if debug is True:
        print "Debug Mode : ON  \t Question 1 (a.)"
        print "i", "\t", "Jv(1)"
        for i in xrange(0, len(J)):
            print i, "\t", "{:.10f}".format(J[i])
    else:
        print "Debug Mode : OFF \t Question 1 (a.)"

def bessel_function(v, x=1):
    j = 0
    b = lambda k : pow(-1, k) * pow(float(x)/2, v + (2 * k)) \
                   / (sm.factorial(k) * sm.factorial(v + k))
    for k in xrange(0, 4):
        j = j + b(k)
    return j

def question_b(debug=True):
    x = linspace(0,3, num=4)   # equally spaced points on interval [0, 3]
    num = lambda v : (x[0]/(v-J[0]))-((3*x[1])/(v-J[1])) + ((x[2]*3)/(v-J[2])) - (x[3]/(v-J[3]))
    den = lambda v : (1/(v-J[0]))- (3/(v-J[1]))+(3/(v-J[2]))-(1/(v-J[3]))

    # the interpolating function from Barycentric Interpolation
    P = [num(x[i]) / den(x[i]) for i in xrange(0, 4)]

    # plot p(v) and Jv(1) on the same system
    plt.plot(x, J, x, P) # plotting t, b separately
    plt.show()

    # plot the error function Jv(1) - p(v)
    err = [jv - pv for jv, pv in zip(J, P)]
    plt.plot(x, err)
    plt.show()

    if debug is True:
        print "Debug Mode : ON  \t Question 1 (b.)"
        print "x                  = ", x
        print "p(v)               = ", P
        print "Jv(1)              = ", J
        print "err = Jv(1) - P(v) = ", err
    else:
        print "Debug Mode : OFF  \t Question 1 (b.)"

def question_c(M4=3.0, debug=True):
    if debug is True:
        print "Debug Mode : ON  \t Question 1 (c.)"
    else:
        print "Debug Mode : OFF \t Question 1 (c.)"

def question_d(debug=True):
    if debug is True:
        print "Debug Mode : ON  \t Question 1 (d.)"
    else:
        print "Debug Mode : OFF \t Question 1 (d.)"

if __name__ == "__main__":
    J = [.0, .0, .0, .0]
    import scipy.special as ss
    import scipy.misc as sm
    from numpy import linspace
    import matplotlib.pyplot as plt

    question_a()
    question_b()
    #question_c()

else:
    import sys
    sys.exit("Run Library as client.")
