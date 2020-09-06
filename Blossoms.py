from numpy import *

def Blossoms(c,k,I,u):
    '''Evaluates S(u) in accordance with De Boor's algorithm.
    :param c: Array of "hot" control points
    :param k: Array of knot points
    :param I: Index of interval that contains u
    :param u: Position
    '''




    #Size of array of "hot control points"
    size = c.shape[0]
    print("Size of array is now" + " " + str(size))
    # Array for storing new control points

    #Should be size (1,2), then 2,2... (i,2)
    newcontrolpoints = zeros((size-1,2))



    #If the size is 1 c is S(u)

    if size == 1:
        print("S(u) is" +str(c))
        return c

    for i in range (1,size):

        #At first call operations are performed 3 times, then 2, then one.

        #New control point at index i is constructed from previous points at index i and i+1

        #Old control points have knot points spanning over a range size-1 (4 indices, 3 indices and so on).
        r = size-1

        #Max index for knotpoints is I+i, min is I+i-range.
        maxindex = I + i
        minindex = maxindex - r

        #Leftmost and rightmost knot for construction of alpha(u)
        urightmostknot = k[maxindex]
        uleftmostknot = k[minindex]

        alphau = (urightmostknot-u)/(urightmostknot-uleftmostknot)

        #Vector of new control points is filled.
        newelement = (alphau) * c[i-1] + (1-alphau) * c[i]

        newcontrolpoints[i-1] = newelement;



        print("New element created")
        print (newcontrolpoints)

    #For every call the size of newcontrolpoints is smaller until s(u) is returned.
    return Blossoms(newcontrolpoints,k,I,u)











