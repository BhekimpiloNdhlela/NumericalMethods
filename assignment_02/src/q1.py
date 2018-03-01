#!/usr/bin/python
def fpi(f, x, k):
    for i in xrange(k):
        print i + 1, "\t{:.15f}".format(x)
        x = f(x)
    print "\n"

if __name__ == "__main__":
    x, k = 1, 10
    f = lambda x : (0.5 * x) + (1 / x)
    g = lambda y : ((2. * x) / 3.) + (2. / (3. * x))
    h = lambda z : (0.75 * x) + (0.5 * x)

    print "The itterations for F(x):"
    fpi(f, x, k)

    print "The itterations for G(x):"
    fpi(g, x, k)

    print "The itterations for H(x):"
    fpi(h, x, k)
else:
    import sys
    sys.exit("please run as client...")
