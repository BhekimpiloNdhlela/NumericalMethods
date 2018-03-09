#!usr/bin/python

def questiona(debug=True):
    J = [bessel(0), bessel(1), bessel(2), bessel(3)]

    if debug is True:
        for i in xrange(0, len(J)):
            print i, "\t", "{:.10f}".format(J[i])

def bessel(v, x=1):
    J = 0
    for k in xrange(0, 4):
        N = pow(-1, k) * pow(float(x)/2, v + (2 * k))
        D = sm.factorial(k) * sm.factorial(v + k)
        J = J + (N / D)
    return J

def questionb():
    pass

if __name__ == "__main__":
    import scipy.special as ss
    import scipy.misc as sm
    questiona()
    questionb()

else:
    sys.exit("Run Library as client.")
