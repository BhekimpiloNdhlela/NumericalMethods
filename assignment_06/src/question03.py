#!/usr/bin/python3
def adam_bashforth_two_step(f, n, t=[1.0, 2.0], w0=4.0):
    W    = zeros((int(n),), dtype=float)
    t    = linspace(t[0], t[1], int(n))
    h    = 1 / float(n)

    W[0] = w0
    W[1] = W[0] + h * f(t[0], W[0])    # w[1] evaluated by euler's method

    for i in range(1, int(n - 1)):
        W[i+1] = W[i] + (0.5*h)*(3*f(t[i], W[i]) - f(t[i-1], W[i-1]))

    # Update global Variables befor returning
    global TWO_STEP_SOLUTIONS
    TWO_STEP_SOLUTIONS.append(W)

    print "Actual Value: @ h = ", h, "\tW[-1] = ", W[-1]
    return W[-1]

def adam_bashforth_mul_step(f, n, t=(1., 2.0), w0=4.0):
    wn   = lambda w0, w1, t0, t1 : -4.0*w0 + 5.0*w1 + h*(4*f(t0, w0) + 2*f(t1, w1))
    W    = zeros((int(n),), dtype=float)
    t    = linspace(t[0], t[1], int(n))
    h    = 1 / float(n)
    W[0] = w0
    W[1] = W[0] + h * f(t[1], W[0])    # w[1] evaluated by euler's method

    for i in range(1, int(n - 1)):
        W[i+1] = -4.0*W[i] + 5.0*W[i-1] + h*(4*f(t[i], W[i]) + 2*f(t[i-1], W[i-1]))

    # Update global Variables befor returning
    global MULTI_STEP_SOLUTIONS
    MULTI_STEP_SOLUTIONS.append(W)
    print "Actual Value: @ h = ", h, "\tW[-1] = ", W[-1]
    return W[-1]

def plot_solution_function():
    I =  lambda t: 4.0*exp(0.5*(1-((t)**2.0)))
    x = linspace(1, 2, 200)
    y = I(x)
    plt.title("")
    plt.ylabel("y = 4.0*exp(0.5*(1-((t)**2.0)))")
    plt.xlabel("time = t)")
    plt.xlim([1, 2])
    plt.plot(x, y, 'c-', linewidth=3)
    plt.show()

def debug(abs_err_2, abs_err_m, debug_status=True):
    if debug_status == True:
        print("Absolute Errors:")
        print("Adam Bashforth Two Steps\tAdam Bashforth Multi Steps")
        for step_2, step_m in zip(abs_err_2, abs_err_m):
            print("{:.20f}".format(step_2) + "\t\t " + "{:.2f}".format(step_m))

# Global Variables
MULTI_STEP_SOLUTIONS = []
TWO_STEP_SOLUTIONS = []

if __name__ == "__main__":
    from numpy import exp, zeros, linspace, arange
    import matplotlib.pyplot as plt

    f       = lambda t, y : -t * y
    I       =  4.0*exp(0.5*(1-((2)**2.0)))
    abs_err = lambda xc   : abs(xc - I)
    N       = [100.0, 200.0, 400.0]
    print "I = ", I
    two_step_abs_err   = [abs_err(adam_bashforth_two_step(f, n)) for n in N]


    print("\n")
    multi_step_abs_err = [abs_err(adam_bashforth_mul_step(f, n)) for n in N]
    for n, err in zip(N, two_step_abs_err):
        print "@ N = ", n,"\t\t{:.10f}".format(err)
    #debug(two_step_abs_err, multi_step_abs_err, debug_status=True)
    #plot_solution_function()
else:
    from sys import exit
    exit("USAGE: question3.py")
