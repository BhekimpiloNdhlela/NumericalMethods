#!/usr/bin/python
def secant_method(x, debug=True):
    appr_list = [1., 0.5, 0., 0., 0., 0., 0., 0., 0.]
    for i in xrange(1, len(appr_list) - 1):
        num = appr_list[i] * appr_list[i - 1] + x
        den = appr_list[i] + appr_list[i - 1]
        appr_list[i + 1] = num / den

    if debug is True:
        print "The Secant Method, DEBUG_MODE: ON:"
        for i in appr_list:
            print "{0:.15f}".format(i)
    return appr_list

def newton_method(x, debug=True):
    appr_list = [1., 0., 0., 0., 0., 0., 0., 0., 0.]
    for i in xrange(len(appr_list) - 1):
        num = appr_list[i]**2 + x
        den = appr_list[i] * 2
        appr_list[i + 1] = num / den

    if debug is True:
        print "The Newton Method, DEBUG_MODE: ON:"
        for i in appr_list:
            print "{0:.15f}".format(i)
    return appr_list

if __name__ == "__main__":
    import math
    new_res, sec_res = newton_method(1. / 9.), secant_method(1. / 9.)
