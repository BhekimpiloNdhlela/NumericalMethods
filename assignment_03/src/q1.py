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
        print "\nDebug Mode : ON  \t Question 1 (a.)"
        print "i", "\t", "Jv(1)"
        for i in xrange(0, len(J)):
            print i, "\t", "{:.10f}".format(J[i])

def bessel_function(v, x=1, j=0):
    b = lambda k : pow(-1, k) * pow(float(x)/2, v + (2 * k)) \
                   / (sm.factorial(k) * sm.factorial(v + k))
    for k in xrange(0, 4):
        j = j + b(k)
    return j

def question_b(debug=True):
    x = linspace(0,3, num=100)   # equally spaced points on interval [0, 3]
    x = [a for a in x if a != 0. if a != 1. if a != 2. if a != 3.]
    # the interpolating function from Barycentric Interpolation
    num = lambda v : (J[0]/v)-((3*J[1])/(v-1.))+((3*J[2])/(v-2.))-\
                     (J[3]/(v-3.))
    den = lambda v : (1./v)-(3./(v-1.))+(3./(v-2.))-(1./(v-3.))
    P = [num(i) / den(i) for i in x]
    global J
    J = [bessel_function(i) for i in x]

    # plot p(v) and Jv(1) on the same system
    func1, = plt.plot(x, J, label="Jv(1)", linestyle='--')
    func2, = plt.plot(x, P, label="P(v)", linestyle='-')
    plt.title('Jv(1) and P(v)')
    plt.ylabel('Jv(1) and P(v)')
    plt.xlabel('v')
    first_legend = plt.legend(handles=[func1], loc=1)
    ax = plt.gca().add_artist(first_legend)
    plt.legend(handles=[func2], loc=4)
    plt.show()
    # plot the error function Jv(1) - p(v)
    error = [jv - pv for jv, pv in zip(J, P)]
    plt.plot(x, error, 'r-')
    plt.title('Error Functioin')
    plt.ylabel('Error: Jv(1) - P(v)')
    plt.xlabel('v')
    plt.show()

    if debug is False:
        print "\nDebug Mode : ON  \t Question 1 (b.)"
        print "i \t\t x \t\t P(x) \t\t Jx(1) \t\t err"
        for i in xrange(len(x)):
            print i, "\t", "{:.10f}".format(x[i]), "\t", \
                           "{:.10f}".format(P[i]), "\t", \
                           "{:.10f}".format(J[i]), "\t", \
                           "{:.10f}".format(error[i])
    est_error = (1. / (4. * n)) * (h**n) * M4
    max_error = sorted(error)[-1] # get max error from questio 1 b.)
    #compare errors is est_error >= max_error
    is_bound_true = est_error >= max_error

    if debug is True:
        print "\nDebug Mode : ON \t Question 1 (c.)"
        print "Estimated Error                \t:", est_error
        print "Maximum Error [Question 1 c.)] \t:", max_error
        print "est_error >= max_error ?       \t", is_bound_true

def question_d(debug=True):
    # coeff of : pi'(x) = 2x^3 -9x^2 + 11x - 3 = 0
    coeff = [2, -9, 11, -3]
    zeros = roots(coeff)

    pi_x = lambda x : x**4 - 6*(x**3) + 11*(x**2) - 6*x
    maxi = [pi_x(x) for x in zeros]
    if debug is True:
        print "\nDebug Mode : ON  \t Question 1 (d.)"
        for i, (zero, max_min) in enumerate(zip(zeros, maxi)):
            print i,'\t', "{:.10f}".format(zero), '\t', \
                          "{:.10f}".format(max_min),'\t',\
                          "{:.10f}".format(fabs(max_min))

if __name__ == "__main__":
    J = [.0, .0, .0, .0]
    from math import fabs
    import scipy.special as ss
    import scipy.misc as sm
    from numpy import (linspace, roots)
    import matplotlib.pyplot as plt

    question_a()
    error = question_b()
    question_c(error)
    question_d()

else:
    import sys
    sys.exit("Run Library as client.")
