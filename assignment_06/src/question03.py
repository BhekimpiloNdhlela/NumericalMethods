#!/usr/bin/python3
def adam_bashforth_two_step(f, n, h, t=[1.0, 2.0], w0=4.0):
    W    = zeros((int(n),), dtype=float)
    t    = linspace(t[0], t[1], int(n))
    W[0] = w0
    W[1] = W[0] + h * f(t[0], W[0])    # w[1] evaluated by euler's method
    for i in range(1, int(n - 1)):
        W[i+1] = W[i] + (0.5*h)*(3*f(t[i], W[i]) - f(t[i-1], W[i-1]))
    return W[-1]

def adam_bashforth_mul_step(f, n, h, t=(1., 2.0), w0=4.0):
    wn   = lambda w0, w1, t0, t1 : -4.0*w0 + 5.0*w1 + h*(4*f(t0, w0) + 2*f(t1, w1))
    W    = zeros((int(n),), dtype=float)
    t    = linspace(t[0], t[1], int(n))
    W[0] = w0
    W[1] = W[0] + h * f(t[1], W[0])    # w[1] evaluated by euler's method
    for i in range(1, int(n - 1)):
        W[i+1] = -4.0*W[i] + 5.0*W[i-1] + h*(4*f(t[i], W[i]) + 2*f(t[i-1], W[i-1]))
    MULTI_STEP_SOLUTIONS.append(W)
    return W[-1]

def plot_solution_function():
    x2 = linspace(1, 2, len(MULTI_STEP_SOLUTIONS[0]))
    plt.subplot(211)
    plt.title("The Approximation of\n dy/dt = -ty by Adam BashForth Multi-Step\nn = 100, h = 0.01")
    plt.ylabel("[LINEAR] Approximation of dy/dt = -ty")
    plt.xlim([1, 2])
    plt.plot(x2, MULTI_STEP_SOLUTIONS[0], 'k-', lw=5, label="h = 0.0025")

    plt.subplot(212)
    plt.xlim([1, 2])
    plt.ylabel("[LOG] Approximation of dy/dt = -ty")
    plt.xlabel("time = t")
    plt.yscale('log')
    plt.plot(x2, MULTI_STEP_SOLUTIONS[0], 'k-', lw=5, label="h = 0.0025")
    plt.show()

def debug(H, N, AE, W, message, debug_status=True):
    if debug_status == True:
        if(message == "2_Step"):
            print("Adam BashForth Two(2) Step Algorithm")
            print("H \t N  \t\tAbs_Err \t W[-1] approx @ t=2")
            for h, n, ae, w in zip(H, N, AE, W):
                print n, "\t{:.4f}\t".format(h), "\t{:.15f}".format(ae), "\t{:.15f}".format(w)
        elif message == "M_Step":
            print("Adam BashForth Multi Step Algorithm")
            print("H \t N  \t\tAbs_Err \t W[-1] approx @ t=2")
            for h, n, ae, w in zip(H, N, AE, W):
                print n, "  {:.4f}  ".format(h), "  {:15E}".format(ae), "  {:15E}".format(w)

# Global Variable
MULTI_STEP_SOLUTIONS = []
if __name__ == "__main__":
    from numpy import exp, zeros, linspace, arange, shape
    import matplotlib.pyplot as plt

    f       = lambda t, y : -t * y
    I       = 4.0*exp(0.5*(1-((2)**2.0)))
    N       = [100.0, 200.0, 400.0]
    H       = [1/ N[0], 1/N[1], 1/N[2]]

    # do for the Adam Bashforth two step Method
    w_ad2s  = [adam_bashforth_two_step(f, n, h) for n, h in zip(N, H)]
    ae_ad2s = [abs(w - I) for w in w_ad2s]
    debug(H, N, ae_ad2s, w_ad2s, "2_Step")

    # do for the Adam Bashforth Multi step Method
    w_adms  = [adam_bashforth_mul_step(f, n, h) for n, h in zip(N, H)]
    ae_adms = [abs(w - I) for w in w_adms]
    debug(H, N, ae_adms, w_adms, "M_Step")
    plot_solution_function()
else:
    from sys import exit
    exit("USAGE: question3.py")
