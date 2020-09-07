from numpy import *
from Blossoms import Blossoms
import matplotlib.pyplot as plt


class Cubic_Spline:

    def __init__(self, knots, control):

        #Control points is array of lists (x and y values)
        self.control_points = control
        #knot points is array of knot points
        self.knot_points = knots

        size = 100

        self.su = zeros((size,2))

        maxval = amax(self.knot_points)

        for i in range(0, size):
            self.su[i] = self.__call__(i*len(knots)/size)


    def __call__(self, u):
        #Find hot interval. Index of the element with higher value - 1.
        I = (self.knot_points > u).argmax()-1
        #print("Index is" + str(I))

        if I == 0:
            return self.control_points[0]
        if I == -1:
            return self.control_points[-1]


        #Find control points d_(I-2) to d_(I+1)
        four_control = self.control_points[I-2:I+2]
        #print("First four points:")
        #print"(four_control)

        #Run deBoor
        #Three times to obtain d[u,u,u]
        s = Blossoms(four_control,self.knot_points,I,u)
        return s




        #Return S(u)


    def plot(self):
        x = linspace(0, 1, len(self.knot_points))
        #plt.plot(x, self.knot_points)
        """
        Plot the cubic spline (self.s_u), its control polygon and the de Boor points
        :return: None
        """
        #plt.plot(self.su[:, 0], self.su[:, 1], 'b')
        #plt.plot(self.control_points[:, 0], self.control_points[:, 1], '-.r')  # control polygon
        #plt.scatter(self.control_points[:, 0], self.control_points[:, 1], color='red')  # de Boor points

        #plt.grid()
        #plt.show()




