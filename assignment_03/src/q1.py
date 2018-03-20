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

def bessel_function(v, x=1, j=0):
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
    func1, = plt.plot(x, J, label="J1(1)", linestyle='-')
    func2, = plt.plot(x, P, label="P(v)", linestyle='-')
    plt.title('Jx(1) and P(x) Function Tittle Should come here')
    plt.ylabel('Jx(1) and P(x)')
    plt.xlabel('x')
    # include legend
    first_legend = plt.legend(handles=[func1], loc=1)
    ax = plt.gca().add_artist(first_legend)
    plt.legend(handles=[func2], loc=4)
    plt.show()
    # plot the error function Jv(1) - p(v)
    err = [jv - pv for jv, pv in zip(J, P)]
    plt.plot(x, err, 'r-')
    plt.title('Error Functioin Tittle Should come here')
    plt.ylabel('Error: Jx(1) - P(x)')
    plt.xlabel('x')
    plt.show()

    if debug is True:
        print "Debug Mode : ON  \t Question 1 (b.)"
        print "x                  = ", x
        print "p(v)               = ", P
        print "Jv(1)              = ", J
        print "err = Jv(1) - P(v) = ", err
    else:
        print "Debug Mode : OFF  \t Question 1 (b.)"
"""
def question_c(M4=3.0, debug=True):
    if debug is True:
        print "Debug Mode : ON  \t Question 1 (c.)"
    else:
        print "Debug Mode : OFF \t Question 1 (c.)"
        print "Debug Mode : ON  \t Question 1 (d.)"

def question_d(debug=True):
    if debug is True:
    else:
        print "Debug Mode : OFF \t Question 1 (d.)"
"""

if __name__ == "__main__":
    J = [.0, .0, .0, .0]
    import scipy.special as ss
    import scipy.misc as sm
    from numpy import linspace
    import matplotlib.pyplot as plt

    question_a()
    question_b()
    #question_c()
    #question_d()

else:
    import sys
    sys.exit("Run Library as client.")
