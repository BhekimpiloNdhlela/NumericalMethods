#!/usr/bin/python
def fpi(f, x, k):
    for i in xrange(k):
        x = f(x)
    return x

if __name__ == "__main__":
    x, k = 1, 1000
    f = lambda x : (0.5 * x) + (1 / x)
    g = lambda y : ((2. * x) / 3.) + (2. / (3. * x))
    h = lambda z : (0.75 * x) + (0.5 * x)

    print "F(x) = ", fpi(f, x, k)
    print "G(x) = ", fpi(g, x, k)
    print "H(x) = ", fpi(h, x, k)
else:
    import sys
    sys.exit("please run as client...")
