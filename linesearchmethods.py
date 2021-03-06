# Some line search methods
from math import inf
from numpy import linspace


def exact_linesearch(f, x, s):
    """
    Exact line search method as described in (3.3) p.31 Nocedal, Wright
    :param f:
    :param x:
    :param s:
    :return:
    """
    alphas = linspace(0, 2, 1000)
    min_alpha = alphas[1]
    min_value = inf
    for alpha in alphas:
        current_value = f(x + alpha * s)
        if current_value < min_value:
            min_alpha = alpha
            min_value = current_value

    return min_alpha


def inexact_linesearch(f, x, s, rho, sigma, tau, chi):
    """
    Determines a_k by inexact line search method satisfying the Wolfe-Powell conditions
    :param f:
    :param x:
    :param s:
    :param rho:
    :param sigma:
    :param tau:
    :param chi:
    :return:
    """
    alpha_L = 0
    alpha_0 = 1
    alpha_U = 10**99

    def f_alpha(alpha):  # defined in section 3.6 Lecture03
        return f(x + alpha * s)

    def f_prim_alpha(alpha):
        epsilon = 0.0001
        n1 = f_alpha(alpha + epsilon)
        n2 = f_alpha(alpha - epsilon)
        res = (n1 - n2) / (2 * epsilon)
        #return (f_alpha(alpha + epsilon) - f_alpha(alpha - epsilon)) / (2 * epsilon)
        return res

    def LC(alpha_0, alpha_L):  # Wolfe-Powell left condition, section 3.8
        return f_prim_alpha(alpha_0) >= sigma*f_prim_alpha(alpha_L)

    def RC(alpha_0, alpha_L):  # Wolfe-Powell right condition, section 3.8
        return f_alpha(alpha_0) <= f_alpha(alpha_L) + rho*(alpha_0 - alpha_L)*f_prim_alpha(alpha_L)

    def extrapolate(alpha_0, alpha_L):  # section 3.11
        return (alpha_0 - alpha_L) * f_prim_alpha(alpha_0) / (f_prim_alpha(alpha_L) - f_prim_alpha(alpha_0))

    def interpolate(alpha_0, alpha_L):  # section 3.11
        return ((alpha_0 - alpha_L)**2 * f_prim_alpha(alpha_L)) / (2 * (f_alpha(alpha_L) - f_alpha(alpha_0) +
                                                                   (alpha_0 - alpha_L)*f_prim_alpha(alpha_L)))

    def block1(alpha_0, alpha_L):  # Block 1, section 3.10
        delta_alpha_0 = extrapolate(alpha_0, alpha_L)
        delta_alpha_0 = max(delta_alpha_0, tau*(alpha_0 - alpha_L))
        delta_alpha_0 = min(delta_alpha_0, chi*(alpha_0 - alpha_L))
        alpha_L = alpha_0
        alpha_0 += delta_alpha_0
        return alpha_L, alpha_0

    def block2(alpha_0, alpha_L, alpha_U):  # Block 2, section 3.10
        alpha_U = min(alpha_0, alpha_U)
        bar_alpha_0 = interpolate(alpha_0, alpha_L)
        bar_alpha_0 = max(bar_alpha_0, alpha_L + tau*(alpha_U - alpha_L))
        bar_alpha_0 = min(bar_alpha_0, alpha_U - tau*(alpha_U - alpha_L))
        alpha_0 = bar_alpha_0
        return alpha_U, alpha_0

    while not (LC(alpha_0, alpha_L) and RC(alpha_0, alpha_L)):  # while we don't satisfy LC AND RC CHECK
        if not LC(alpha_0, alpha_L):
            alpha_L, alpha_0 = block1(alpha_0, alpha_L)
        else:
            alpha_U, alpha_0 = block2(alpha_0, alpha_L, alpha_U)

    return alpha_0  # , f_alpha(alpha_0)
