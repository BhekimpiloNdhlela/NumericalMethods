#   X = GAUSS(N) returns N Legendre points X in (-1,1).
#
#   X, C = GAUSS(N) returns also a vector C of weights for
#   Gauss-Legendre quadrature.
#
#   X, C = GAUSS(N, [A, B]) returns the nodes and weeights
#   for the interval [A, B].

import numpy as np

def gauss(N, dom=[-1,1]):
    x = np.zeros(shape=(N,1))
    for k in range(N):
        x[k] = -np.cos((0.5+k)*np.pi/N)
    tol = 1e-10
    dx = 1 + 0 *x
    # Loop until convergence:
    while np.linalg.norm(dx, np.inf) > tol:
        # Recurrence relation for Legendre polynomials:
        Pm2 = 1
        Pm1 = x
        for n in range(1,N):
            P = ( (2*n+1)*Pm1*x - n*Pm2 ) / (n+1)
            Pm2 = Pm1
            Pm1 = P

        # Derivative.  See NIST (18.9.17)
        dPdx = -N * (x*P - Pm2) / (1 - x**2)

        # Newton step:
        dx = -P / dPdx;
        # Newton update:
        x = x + dx;

    # Weights
    c = 2 / ( (1-x**2) * dPdx**2 );

    # Scale
    a = dom[0];
    b = dom[1];
    x = .5*(b-a)*x + .5*(b+a);
    c = .5*(b-a)*c;

    return (x, c)

if __name__ == "__main__":
    x, c = gauss(5, [-1, 1])
    print 'x = ', x
    print 'c = ', c
