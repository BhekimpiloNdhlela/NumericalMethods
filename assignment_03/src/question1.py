#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 03 question 1 (a.)
since   : Friday-09-03-2018
"""
def questiona(debug=True):
    global J
    J = [bessel_function(i) for i in xrange(0, 4)]
    if debug is True:
        print "Question 1 (a.)"
        for i in xrange(0, len(J)):
            print i, "\t", "{:.10f}".format(J[i])
    print "\n"

def bessel_function(v, x=1):
    j = 0
    global b
    for k in xrange(0, 4):
        j = j + (b(k))
    return j

def questionb(p, debug=True):
    x = linspace(0,3, num=4)
    #y = [ for i, j in J]
    print x
    if debug is True:
        print "Question 1 (b.)"
        #for i, j, k in emumarate():
        #    print i, j, j

if __name__ == "__main__":
    J = [.0, .0, .0, .0]
    import scipy.special as ss
    import scipy.misc as sm
    from numpy import linspace
    import matplotlib.pyplot as plt

    b = lambda k : pow(-1, k) * pow(1./2, v + (2 * k)) \
                   / (sm.factorial(k) * sm.factorial(v + k))
    '''
    This is a cubic interpolating polynomial, although it may
    not look like it :-)!
    '''
    p = lambda x : y1/(x-y1)-(3*y2)/(x-x1)+(y3*3)/(x-x3) - y4/(x-x4) \
                   / (1/(x-x1)-3/(x-x1)+3/(x-x3)-y4/(x-x4))


    questiona()
    questionb(p)

else:
    sys.exit("Run Library as client.")
