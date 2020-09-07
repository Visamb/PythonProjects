# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from  scipy import *
from  numpy import *
from Cubic_Spline import *
from Nfunc import Nfunc
from matplotlib import pyplot as plt

test_control = array( [[-40, 20],[-40, 20],[-40, 20], [-20, 0], [-100, -15], [-22, -62], [8, -78], [57, -30], [15, 8], [18, -3], [40, 17],[40, 17],[40, 17]])
test_knots = array([0,0,0, 1, 2, 3, 4, 5, 6, 7, 8,8,8])
test_u = 3

testSpline = Cubic_Spline(test_knots,test_control)
testSpline.plot()
su = testSpline(test_u)
#print(su)




size = 1000
xspace = linspace(0,8,size)
nvals = zeros(size)
nvals2 = zeros(size)
maxval = amax(test_knots)
for i in range(0, size):
 nvals[i] = Nfunc(test_knots, 2, 3, i*8/size)
 nvals2[i] = Nfunc(test_knots, 2, 3, i*8/size)

print(str(nvals.shape))
print(str(xspace.shape))

plt.plot(xspace, nvals, 'b')
plt.plot(xspace, nvals2, 'r')
plt.grid()
plt.show()









