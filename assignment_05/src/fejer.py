#   X = FEJER(N) returns N Chebyshev points X in (-1,1).
#
#   X, W = FEJER(N) returns also a vector W of weights for
#   Fejer quadrature.
#
#   X, W = FEJER(N, [A, B]) returns the nodes and weights
#   for the interval [A, B].

import numpy as np

def fejer(N, dom=[-1,1]):
    t = np.zeros(shape=(N,1))
    x = np.zeros(shape=(N,1))
    for k in range(N):
        t[k] = (0.5+k)*np.pi/N;
        x[k] = -np.cos(t[k])

    # Weights
    V_trans = np.zeros(shape=(N,N))
    for j in range(N):
        for k in range(N):
            V_trans[j][k] = np.cos(j*t[k]);
    rhs = np.zeros(shape=(N,1))
    for j in range(0, N, 2):
        rhs[j] = 2./(1.-j*j);
    c = np.linalg.solve(V_trans, rhs);

    # Scale
    a = dom[0];
    b = dom[1];
    x = .5*(b-a)*x + .5*(b+a);
    c = .5*(b-a)*c;

    return (x, c)
if __name__ == "__main__":
    x, c = fejer(5, [-1, 1])
    print 'x = ', x
    print 'c = ', c
