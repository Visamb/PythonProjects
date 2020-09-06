# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from  scipy import *
from  numpy import *
from Cubic_Spline import *



test_control = array( [[-40, 20],[-40, 20],[-40, 20], [-20, 0], [-100, -15], [-22, -62], [8, -78], [57, -30], [15, 8], [18, -3], [40, 17],[40, 17],[40, 17]])
test_knots = array([0,0,0, 1, 2, 4, 5, 6, 9, 11, 12,12,12])
test_u = 12

testSpline = Cubic_Spline(test_knots,test_control)
testSpline.plot()
su = testSpline(test_u)
print(su)






