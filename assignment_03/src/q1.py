#!usr/bin/python
"""
author  : Bhekimpilo Ndhlela
author  : 18998712
module  : Applied Mathematics(Numerical Methods) TW324
task    : computer assignment 03 question 1 (a. to d.)
since   : Friday-09-03-2018
"""
def questiona(debug=True):
    global J
    J = [bessel_function(i) for i in xrange(0, 4)]
    if debug is True:
        print "Question 1 (a.)"
        print "i", "\t", "Jv(1)"
        for i in xrange(0, len(J)):
            print i, "\t", "{:.10f}".format(J[i])
    print "\n"

def bessel_function(v, x=1):
    j = 0
    b = lambda k : pow(-1, k) * pow(float(x)/2, v + (2 * k)) \
                   / (sm.factorial(k) * sm.factorial(v + k))
    for k in xrange(0, 4):
        j = j + b(k)
    return j

def questionb(debug=True):
    x = linspace(0,3, num=10)
    print "len(x) =",len(x), "x = ", x
    '''
    This is a cubic interpolating polynomial, although it may
    not look like it :-)!
    '''
    #y = lambda v : J[0]/(v-x[0])-(3*J[1])/(v-x[1])+(J[2]*3)/(v-x[2]) - J[3]/(v-x[3]) \
    #               / (1/(v-x[0])-3/(v-x[1])+3/(v-x[2])-1/(v-x[3]))

    #p = [y(i) for i in x]



    #if debug is True:
        #print "Question 1 (b.)"
        #for i, j, k in emumarate():
        #    print i, j, j

if __name__ == "__main__":
    J = [.0, .0, .0, .0]
    import scipy.special as ss
    import scipy.misc as sm
    from numpy import linspace
    import matplotlib.pyplot as plt
    questiona()
    questionb()

else:
    import sys
    sys.exit("Run Library as client.")
