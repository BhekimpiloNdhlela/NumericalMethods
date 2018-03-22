#!usr/bin/python
def __bessel_function__(v, x=1, j=0):
    b = lambda k : pow(-1, k) * pow(float(x)/2, v + (2 * k)) \
                   / (sm.factorial(k) * sm.factorial(v + k))
    for k in xrange(0, 4):
        j = j + b(k)
    return j

def question_i(a=0.0, b=3.0, N=100):
    X = linspace(a, b, num=N, endpoint=True)
    J = [__bessel_function__(i) for i in X]
    data_p = [__bessel_function__(i) for i in xrange(0, 4)]
    cs = CubicSpline(X, J, bc_type="not-a-knot")

    error = [j - p for j, p in zip(J, cs(X))]
    plt.title("CS Interpolants: Not-a-Knot Conditions")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot([0,1,2,3], data_p, 'o', label='data points')
    plt.plot(X, cs(X), '--', label='CS Not-a-Knot')
    plt.plot(X, error, '-', label="error")
    plt.legend(loc='up right', ncol=2)
    plt.show()

def question_ii(a=0.0, b=3.0, N=100):
    X = linspace(a, b, num=N)
    J = [__bessel_function__(i) for i in X]
    cs = CubicSpline(X, J, bc_type="clamped")
    error = [j - p for j, p in zip(J, cs(X))]
    data_p = [__bessel_function__(i) for i in xrange(0, 4)]
    plt.title("CS Interpolants: Clamped CS Conditions")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot([0,1,2,3], data_p, 'o', label='data points')
    plt.plot(X, cs(X), '--', label='CS clamped')
    plt.plot(X, error, '-', label="error")
    plt.legend(loc='up right', ncol=2)
    plt.show()

if __name__ == "__main__":
    from scipy.interpolate import CubicSpline
    import matplotlib.pyplot as plt
    from numpy import linspace
    import scipy.misc as sm
    from math import pow

    question_i()
    question_ii()
else:
    import sys
    sys.exit("Please run this library as client.")
