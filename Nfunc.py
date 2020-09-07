from numpy import *

def Nfunc(knots, i, k, u):

    if k == 0:
        return 1.0 if knots[i-1] <= u < knots[i] else 0.0
    if knots[i + k -1] == knots[i-1]:
        c1 = 0.0
    else:
        c1 = (u - knots[i-1]) / (knots[i-1 + k] - knots[i-1]) * Nfunc(knots, i, k-1, u)
    if knots[i + k] == knots[i]:
        c2 = 0.0
    else:
        c2 = (knots[i + k] - u) / (knots[i + k] - knots[i]) * Nfunc(knots, i+1, k-1, u)
    return c1 + c2

