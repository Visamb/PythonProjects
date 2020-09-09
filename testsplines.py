import unittest

from numpy import *

import CubicSpline as csp


class TestSplines(unittest.TestCase):
    test_control = array(
    [[-17, 9],
     [-40, 20],
     [-20, 0],
     [-100, -15],
     [-22, -62],
     [8, -78],
     [57, -30],
     [15, 8],
     [18, -3],
     [40, 17]])
    test_knots = array([0, 0, 0, 1, 2, 3, 6, 9, 11, 12, 12, 12])
    inp1 = (test_control, test_knots)

    def testinit(self):
        spline = csp.CubicSpline(*self.inp1)
        control = vstack([self.test_control[0], self.test_control[0], self.test_control, self.test_control[-1], self.test_control[-1]])
        knot1 = spline.knot_points
        control1 = spline.control_points
        assert (self.test_knots == spline.knot_points).all()
        assert (control == spline.control_points).all()

    """def testblossoms(self):
        spline = csp.CubicSpline(*self.inp1)
        su = spline.blossoms(*self.test_control[:4], *self.test_knots, 0, spline.control_points[0])
        first = self.test_control[0]
        assert (first == su).all()"""


if __name__ == '__main__':
    unittest.main()
