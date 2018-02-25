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

def correct_digs(list, accurate_num, debug=True):
    correct_digits = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in xrange(len(list)):
        correct_digits[i] = abs(list[i] - accurate_num)

    if debug is True:
        print "  Computed Value    Absolute Error"
        for i in xrange(len(correct_digits)):
            print "{0:.15f}".format(list[i]), "{0:.15f}".format(correct_digits[i])

    return correct_digits

import math
new_res       = newton_method(1. / 9., False)
sec_res       = secant_method(1. / 9., False)
sec_corr_digs = correct_digs(sec_res, math.sqrt(1./9.))
new_corr_digs = correct_digs(new_res, math.sqrt(1./9.))
